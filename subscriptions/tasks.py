from celery import shared_task
from django.utils import timezone
from .models import Subscription
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

@shared_task
def check_subscription_status():
    """Check and update subscription statuses"""
    subscriptions = Subscription.objects.filter(status='active')
    for subscription in subscriptions:
        try:
            stripe_sub = stripe.Subscription.retrieve(
                subscription.stripe_subscription_id
            )
            if stripe_sub.status != subscription.status:
                subscription.status = stripe_sub.status
                subscription.save()
        except stripe.error.StripeError as e:
            print(f"Error checking subscription {subscription.id}: {str(e)}")

@shared_task
def handle_trial_ending_soon():
    """Notify users about trials ending soon"""
    tomorrow = timezone.now() + timezone.timedelta(days=1)
    trial_ending = Subscription.objects.filter(
        trial_end__lte=tomorrow,
        status='trialing'
    )
    for subscription in trial_ending:
        # Send notification to user (implement your notification logic here)
        print(f"Trial ending soon for subscription {subscription.id}")

@shared_task
def clean_cancelled_subscriptions():
    """Clean up cancelled subscriptions after certain period"""
    month_ago = timezone.now() - timezone.timedelta(days=30)
    Subscription.objects.filter(
        status='canceled',
        updated_at__lte=month_ago
    ).delete() 
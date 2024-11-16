import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Payment, Invoice
from subscriptions.models import Subscription
from accounts.models import User

@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event.type == 'payment_intent.succeeded':
        handle_payment_intent_succeeded(event.data.object)
    elif event.type == 'invoice.paid':
        handle_invoice_paid(event.data.object)
    elif event.type == 'customer.subscription.deleted':
        handle_subscription_deleted(event.data.object)
    elif event.type == 'customer.subscription.updated':
        handle_subscription_updated(event.data.object)

    return HttpResponse(status=200)

def handle_payment_intent_succeeded(payment_intent):
    Payment.objects.create(
        user=User.objects.get(email=payment_intent.customer_email),
        stripe_payment_id=payment_intent.id,
        amount=payment_intent.amount / 100,  # Convert from cents
        status='succeeded'
    )

def handle_invoice_paid(invoice):
    Invoice.objects.create(
        user=User.objects.get(email=invoice.customer_email),
        stripe_invoice_id=invoice.id,
        amount=invoice.amount_paid / 100,
        status='paid',
        due_date=invoice.due_date
    )

def handle_subscription_deleted(subscription):
    sub = Subscription.objects.get(stripe_subscription_id=subscription.id)
    sub.status = 'canceled'
    sub.save()

def handle_subscription_updated(subscription):
    sub = Subscription.objects.get(stripe_subscription_id=subscription.id)
    sub.status = subscription.status
    sub.save() 
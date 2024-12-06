from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Subscription, Plan
from .serializers import SubscriptionSerializer, PlanSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscription_dashboard(request):
    user_subscriptions = Subscription.objects.filter(user=request.user)
    active_subscription = user_subscriptions.filter(status='active').first()
    available_plans = Plan.objects.filter(is_active=True)
    
    return Response({
        'active_subscription': SubscriptionSerializer(active_subscription).data if active_subscription else None,
        'subscription_history': SubscriptionSerializer(user_subscriptions, many=True).data,
        'available_plans': PlanSerializer(available_plans, many=True).data
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscription_analytics(request):
    user_subscriptions = Subscription.objects.filter(user=request.user)
    
    return Response({
        'total_subscriptions': user_subscriptions.count(),
        'active_subscriptions': user_subscriptions.filter(status='active').count(),
        'trial_subscriptions': user_subscriptions.filter(status='trialing').count(),
        'subscription_timeline': SubscriptionSerializer(
            user_subscriptions.order_by('-created_at')[:10], 
            many=True
        ).data
    }) 
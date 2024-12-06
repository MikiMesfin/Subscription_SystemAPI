from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, SubscriptionViewSet
from . import dashboard_views

router = DefaultRouter()
router.register(r'plans', PlanViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard_views.subscription_dashboard, name='subscription-dashboard'),
    path('analytics/', dashboard_views.subscription_analytics, name='subscription-analytics'),
] 
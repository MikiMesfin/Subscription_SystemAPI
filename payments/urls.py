from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, InvoiceViewSet
from . import dashboard_views

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard_views.payment_dashboard, name='payment-dashboard'),
    path('billing/', dashboard_views.billing_overview, name='billing-overview'),
] 
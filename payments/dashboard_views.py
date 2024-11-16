from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from .models import Payment, Invoice
from .serializers import PaymentSerializer, InvoiceSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_dashboard(request):
    user_payments = Payment.objects.filter(user=request.user)
    user_invoices = Invoice.objects.filter(user=request.user)
    
    return Response({
        'recent_payments': PaymentSerializer(
            user_payments.order_by('-created_at')[:5], 
            many=True
        ).data,
        'pending_invoices': InvoiceSerializer(
            user_invoices.filter(status='unpaid'), 
            many=True
        ).data,
        'total_spent': user_payments.filter(status='succeeded').aggregate(
            total=Sum('amount')
        )['total'] or 0,
        'payment_history': PaymentSerializer(
            user_payments.order_by('-created_at'), 
            many=True
        ).data
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def billing_overview(request):
    user_invoices = Invoice.objects.filter(user=request.user)
    
    return Response({
        'total_invoices': user_invoices.count(),
        'paid_invoices': user_invoices.filter(status='paid').count(),
        'unpaid_invoices': user_invoices.filter(status='unpaid').count(),
        'recent_invoices': InvoiceSerializer(
            user_invoices.order_by('-created_at')[:5], 
            many=True
        ).data
    }) 
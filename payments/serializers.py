from rest_framework import serializers
from .models import Payment, Invoice

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'user', 'amount', 'status', 'created_at')
        read_only_fields = ('id', 'created_at')

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id', 'user', 'payment', 'amount', 'status', 'due_date', 'created_at')
        read_only_fields = ('id', 'created_at') 
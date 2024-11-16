from django.contrib import admin
from .models import Payment, Invoice

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__email', 'stripe_payment_id')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'due_date')
    list_filter = ('status',)
    search_fields = ('user__email', 'stripe_invoice_id')

from django.db import models
from accounts.models import User

# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_payment_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('succeeded', 'Succeeded'),
            ('failed', 'Failed'),
            ('pending', 'Pending'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
    stripe_invoice_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('paid', 'Paid'),
            ('unpaid', 'Unpaid'),
            ('void', 'Void'),
        ]
    )
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

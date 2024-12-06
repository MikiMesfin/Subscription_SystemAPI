from rest_framework import serializers
from .models import Plan, Subscription

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'name', 'description', 'price', 'interval', 'features')
        read_only_fields = ('id',)

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'user', 'plan', 'status', 'start_date', 'end_date', 'trial_end')
        read_only_fields = ('id',) 
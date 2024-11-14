from rest_framework import serializers
from .models import User, BusinessProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_business')
        read_only_fields = ('id',)

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = ('id', 'company_name', 'tax_id', 'address', 'created_at')
        read_only_fields = ('id', 'created_at') 
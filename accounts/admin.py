from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, BusinessProfile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_business', 'is_staff')
    list_filter = ('is_business', 'is_staff', 'is_active')
    search_fields = ('email', 'username')

@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'created_at')
    search_fields = ('company_name', 'user__email')

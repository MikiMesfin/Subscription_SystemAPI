from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BusinessProfileViewSet, LoginView, LogoutView, get_user_dashboard

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'business-profiles', BusinessProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', get_user_dashboard, name='user-dashboard'),
] 
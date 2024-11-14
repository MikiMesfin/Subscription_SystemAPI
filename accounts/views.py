from django.shortcuts import render
from rest_framework import viewsets, permissions, views, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, BusinessProfile
from .serializers import UserSerializer, BusinessProfileSerializer
from subscriptions.serializers import SubscriptionSerializer
from payments.serializers import PaymentSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

class BusinessProfileViewSet(viewsets.ModelViewSet):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return BusinessProfile.objects.all()
        return BusinessProfile.objects.filter(user=self.request.user)

class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_400_BAD_REQUEST
            )

class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Successfully logged out'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_dashboard(request):
    user = request.user
    subscriptions = user.subscription_set.all()
    payments = user.payment_set.all()
    
    return Response({
        'user': UserSerializer(user).data,
        'business_profile': BusinessProfileSerializer(user.businessprofile).data if hasattr(user, 'businessprofile') else None,
        'active_subscription': SubscriptionSerializer(subscriptions.filter(status='active').first()).data if subscriptions.exists() else None,
        'recent_payments': PaymentSerializer(payments.order_by('-created_at')[:5], many=True).data
    })

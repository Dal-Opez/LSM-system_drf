from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserCreateAPIView, UserProfileAPIView, UserDeleteAPIView, UserListAPIView, PaymentViewSet
from users.apps import UsersConfig


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='profile-detail'),
    path('profile/', UserProfileAPIView.as_view(), name='profile-current'),
    path('profile/delete/', UserDeleteAPIView.as_view(), name='profile-delete'),
    path('', UserListAPIView.as_view(), name='users-list'),
]

urlpatterns += router.urls
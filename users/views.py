from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from rest_framework.generics import CreateAPIView


# Create your views here.
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('payment_date', 'paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('payment_date',)
    ordering = ('-payment_date',)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
from rest_framework.serializers import ModelSerializer
from users.models import Payment, User
from django.contrib.auth.hashers import make_password


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'phone', 'city', 'avatar']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
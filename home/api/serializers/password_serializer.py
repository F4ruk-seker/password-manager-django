from rest_framework import serializers
from home.models import UserPassword
from .provider_serializer import ProviderSerializer


class PasswordSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer()

    class Meta:
        model = UserPassword
        fields = '__all__'


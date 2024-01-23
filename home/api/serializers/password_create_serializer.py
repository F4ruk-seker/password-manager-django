from rest_framework import serializers
from home.models import UserPassword


class PasswordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPassword
        fields = '__all__'


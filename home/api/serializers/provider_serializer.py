from rest_framework import serializers
from home.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    application_type = serializers.SerializerMethodField()

    @staticmethod
    def get_application_type(obj):
        return {
            'id': obj.provider_type,
            'label': obj.ProviderType(obj.provider_type).label
        }

    class Meta:
        model = Provider
        fields = '__all__'


from rest_framework.generics import CreateAPIView
from home.api.serializers import PasswordCreateSerializer
from home.models import UserPassword


class PasswordCreateView(CreateAPIView):
    serializer_class = PasswordCreateSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from home.models import UserPassword
from home.api.serializers import PasswordCreateSerializer
from home.api.permissions import IsOwner


class PasswordRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # authentication_classes =
    permission_classes = [IsOwner]
    serializer_class = PasswordCreateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return UserPassword.objects.filter(user_id=self.request.user).all()


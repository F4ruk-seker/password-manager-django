from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from home.models import UserPassword
from home.api.serializers import PasswordSerializer


class PasswordsListView(ListAPIView):
    model = UserPassword
    serializer_class = PasswordSerializer
    # authentication_classes = [IsAuthenticated,]

    def get_queryset(self):
        print(f"user -> {self.request.user}")
        return UserPassword.objects.filter(user_id=self.request.user).all()


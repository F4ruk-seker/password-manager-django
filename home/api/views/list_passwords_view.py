from rest_framework.generics import ListAPIView
from home.models import UserPassword
from home.api.serializers import PasswordSerializer


class PasswordsListView(ListAPIView):
    model = UserPassword
    serializer_class = PasswordSerializer

    def get_queryset(self):
        return UserPassword.objects.filter(user_id=self.request.user).all()


from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


appname: str = 'api'
urlpatterns: list = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password/', include('home.api.urls'))
]


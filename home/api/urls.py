from django.urls import path
from home.api import views


appname: str = 'api'
urlpatterns: list = [
    path('all', views.PasswordsListView.as_view()),
    path('create', views.PasswordCreateView.as_view()),
    path('<id>', views.PasswordRetrieveUpdateDestroyAPIView.as_view())
]


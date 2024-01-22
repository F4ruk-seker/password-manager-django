from django.urls import path
from home.api import views


appname: str = 'api'
urlpatterns: list = [
    path('all', views.PasswordsListView.as_view()),
    # path('<x>/edit/', views.PasswordsListView.as_view())
]


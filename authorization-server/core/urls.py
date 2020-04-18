from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register),
    path('user/', views.UserView.as_view(), name='user'),
]

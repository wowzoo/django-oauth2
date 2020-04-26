from django.urls import path
from . import views


urlpatterns = [
    path('me/', views.UserView.as_view(), name='me'),
    path('register/', views.RegisterView.as_view(), name='register'),
]

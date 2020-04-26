from django.urls import path
from . import views


urlpatterns = [
    path('token/', views.RetrieveTokenView.as_view(), name='token'),
    path('token/refresh/', views.RefreshTokenView.as_view(), name='token_refresh'),
    path('token/revoke/', views.RevokeTokenView.as_view(), name='token_revoke'),
    path('me/', views.UserView.as_view(), name='me'),
    path('register/', views.RegisterView.as_view(), name='register'),
]

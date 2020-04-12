from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnicornViewSet

router = DefaultRouter()
router.register(r'unicorn', UnicornViewSet)

urlpatterns = [
    path("", include(router.urls))
]

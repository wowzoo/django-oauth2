import logging

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .serializers import CreateUserSerializer, UserSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logger.info(request.data)

        return Response(status.HTTP_200_OK)

    def get(self, request):
        logger.info(request.query_params)
        logger.info(request.META)

        return Response(status.HTTP_200_OK)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Registers user to the server. Input should be in the format:
        {"username": "username", "password": "1234abcd"}
        """
        # Put the data from the request into the serializer
        serializer = CreateUserSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            # If it is valid, save the data (creates a user).
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

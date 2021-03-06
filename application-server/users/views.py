import requests
import logging

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.conf import settings
from rest_framework.views import APIView


logger = logging.getLogger(__name__)


class RetrieveTokenView(APIView):
    """
    View for login
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Gets tokens with username and password. Input should be in the format:
        {"username": "username", "password": "1234abcd"}
        """
        res = requests.post(
            f'{settings.AUTHORIZATION_SERVER_URL}/o/token/',
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': settings.CLIENT_ID,
                'client_secret': settings.CLIENT_SECRET
            },
        )

        return Response(res.json())


class RevokeTokenView(APIView):
    """
    View for logout
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Method to revoke tokens.
        {"token": "<token>"}
        """
        res = requests.post(
            f'{settings.AUTHORIZATION_SERVER_URL}/o/revoke_token/',
            data={
                'token': request.data['token'],
                'client_id': settings.CLIENT_ID,
                'client_secret': settings.CLIENT_SECRET,
            },
        )

        # If it goes well return success message (would be empty otherwise)
        if res.status_code == requests.codes.ok:
            return Response({'message': 'token revoked'}, res.status_code)

        # Return the error if it goes badly
        return Response(res.json(), res.status_code)


class RefreshTokenView(APIView):
    """
    View for refresh token
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Registers user to the server. Input should be in the format:
        {"refresh_token": "<token>"}
        """
        r = requests.post(
            f'{settings.AUTHORIZATION_SERVER_URL}/o/token/',
            data={
                'grant_type': 'refresh_token',
                'refresh_token': request.data['refresh_token'],
                'client_id': settings.CLIENT_ID,
                'client_secret': settings.CLIENT_SECRET,
            },
        )

        return Response(r.json())


class UserView(APIView):
    """
    View to show user in the system.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        logger.info(request.auth)
        logger.info(request.META)

        res = requests.get(
            f'{settings.AUTHORIZATION_SERVER_URL}/users/me/',
        )

        return Response(res.json, res.status_code)


class RegisterView(APIView):
    """
    View for user register
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Registers user to the server. Input should be in the format:
        {"username": "username", "password": "1234abcd"}
        """
        res = requests.post(
            f'{settings.AUTHORIZATION_SERVER_URL}/users/register/',
            data={
                'username': request.data['username'],
                'password': request.data['password']
            }
        )

        if res.status_code == status.HTTP_201_CREATED:
            # Then we get a token for the created user.
            # This could be done differently
            r = requests.post(
                f'{settings.AUTHORIZATION_SERVER_URL}/o/token/',
                data={
                    'grant_type': 'password',
                    'username': request.data['username'],
                    'password': request.data['password'],
                    'client_id': settings.CLIENT_ID,
                    'client_secret': settings.CLIENT_SECRET,
                },
            )
            return Response(r.json())
        else:
            return Response(res.json(), res.status_code)






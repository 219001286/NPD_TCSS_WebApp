from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from accounts.api.serializers import AccountRegisterSerializer
from accounts import models


@api_view(['POST', ])
def AccountLogoutView(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST',])
def AccountRegistrationView(request):
    if request.method == 'POST':
        serializer = AccountRegisterSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Successful!"
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['email'] = account.email
            data['telephone'] = account.telephone
            data['institute'] = account.institute

            token = Token.objects.get(user=account).key
            data['token'] = token

        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)
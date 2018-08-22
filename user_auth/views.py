from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response(
                {'error': 'Please provide both username and password'},
                status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)

class SignUp(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        if username is None or password is None or email is None:
            return Response(
                {'message': '', 'error': 'Please provide username, password and email'},
                status=HTTP_400_BAD_REQUEST)

        user = User.objects.filter(Q(username=username) | Q(email=email)).first()
        if user:
            return Response(
                {'message': '',
                 'error': 'User with given information already exist'},
                status=HTTP_400_BAD_REQUEST)

        user = User.objects.create(username='test_user1', email=email)
        user.set_password('12345')
        user.save()

        return Response({'message':{'user_id': user.id, 'success': True}, 'error':''})

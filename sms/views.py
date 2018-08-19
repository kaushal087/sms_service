from django.shortcuts import render

# Create your views here.

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



class InboundSMS(APIView):

    def post(self, request):
        return Response({'type':'inbound'},
                        status=HTTP_200_OK)

class OutboundSMS(APIView):

    def post(self, request):
        return Response({'type': 'outbound'},
                        status=HTTP_200_OK)

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from .helpers import InboundSmsHelper, OutboundSmsHelper, CacheHelper

class InboundSMS(APIView):

    def post(self, request):
        data = request.data
        InboundSmsHelper().validate(data)
        CacheHelper().set(data=data)
        return Response({'message':'inbound sms is ok' , "error":""},
                        status=HTTP_200_OK)

class OutboundSMS(APIView):

    def post(self, request):
        data = request.data
        OutboundSmsHelper().validate(data=data)
        if CacheHelper().get(data=data):
            error_message = 'sms from {_from} and to {_to} blocked by STOP request'.format(
                                 _from=data.get('from'), _to=data.get('to'))
            return Response({'message': '','error': error_message},
                            status=HTTP_400_BAD_REQUEST)
        return Response({'message':'outbound sms is ok', "error":""},
                        status=HTTP_200_OK)

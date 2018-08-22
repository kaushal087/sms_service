from rest_framework.exceptions import Throttled
from rest_framework.views import exception_handler
from rest_framework.serializers import ValidationError
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if not response:
        message = {"message": "","error": "unknown failure"}
        return Response(message,status=500)
    request = context.get('request')

    if isinstance(exc, Throttled):
        custom_response_data = {"message": "", "error": "limit reached for from {_from}".format(_from=request.data.get('from', ''))}
        response.data = custom_response_data
    if not isinstance(exc, Throttled) and not isinstance(exc, ValidationError):
        custom_response_data = {"message": "","error": "unknown failure"}
        response.data = custom_response_data

    if isinstance(exc, ValidationError):
        custom_response_data = {"message": "", "error": response.data}
        response.data = custom_response_data

    return response
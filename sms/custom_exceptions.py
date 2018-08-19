from rest_framework.exceptions import Throttled
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    request = context.get('request')

    if isinstance(exc, Throttled):
        custom_response_data = {"message": "", "error": "limit reached for from {_from}".format(_from=request.data.get('from', ''))}
        response.data = custom_response_data
    return response
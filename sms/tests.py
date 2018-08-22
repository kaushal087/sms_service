# from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
from django.test import Client
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.contrib.auth import get_user_model



INBOUND_VALID_DATA = { "to": "123456789", "from":"987654321", "text":"Hello World"}
INBOUND_VALID_RESPONSE = { "message": "inbound sms is ok", "error": "" }

INVALID_DATA1 = {}
INVALID_DATA1_RESPONSE = {"message":"","error":{"to":["to is missing"],"text":["text is missing"],"from":["from is missing"]}}


INVALID_DATA2 = {"to": "123", "from":"1", "text":""}
INVALID_DATA2_RESPONSE = {"message":"","error":{"to":["to is invalid"],"text":["text is invalid"],"from":["from is invalid"]}}


ERROR_DATA = ''
UNEXPECTED_ERROR_RESPONSE = {"message":"","error":"unknown failure"}


OUTBOUND_VALID_DATA = { "to": "123456789", "from":"987654321", "text":"Hello World"}
OUTBOUND_VALID_RESPONSE = { "message": "outbound sms is ok", "error": "" }


class TestInboundSMS(TestCase):

    def setUp(self):
        User = get_user_model()
        user = User.objects.create(username='test_user1')
        user.set_password('12345')
        user.save()

        self.user = user
        token, _ = Token.objects.get_or_create(user=self.user)
        # print(token.user)
        self.valid_token = token.key
        self.invalid_token = 'this_invalid_token'

    def test_invalid_token_access_denied(self):
        """
        Testing bad auth, API request with invalid token
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.invalid_token)
        # print(client.__dict__)
        response = client.post('/inbound/sms/', INBOUND_VALID_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_token_access_success(self):
        """
        Testing good auth, API request with valid token
        """

        client = APIClient()
        authori = 'Token ' + self.valid_token
        client.credentials(HTTP_AUTHORIZATION=authori)
        response = client.post('/inbound/sms/', INBOUND_VALID_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_success_request(self):
        client = APIClient()
        authori = 'Token ' + self.valid_token
        client.credentials(HTTP_AUTHORIZATION=authori)
        response = client.post('/inbound/sms/', INBOUND_VALID_DATA,
                                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, INBOUND_VALID_RESPONSE)

    def test_variable_required_request(self):
        client = APIClient()
        authori = 'Token ' + self.valid_token
        client.credentials(HTTP_AUTHORIZATION=authori)
        response = client.post('/inbound/sms/', INVALID_DATA1,
                               format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, INVALID_DATA1_RESPONSE)

    def test_invalid_data_request(self):
        client = APIClient()
        authori = 'Token ' + self.valid_token
        client.credentials(HTTP_AUTHORIZATION=authori)
        response = client.post('/inbound/sms/', INVALID_DATA2,
                               format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, INVALID_DATA2_RESPONSE)

    # def test_unexpected_error(self):
    #     client = APIClient()
    #     authori = 'Token ' + self.valid_token
    #     client.credentials(HTTP_AUTHORIZATION=authori)
    #     response = client.post('/inbound/sms/', ERROR_DATA,
    #                            format='json')
    #     self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    #     self.assertEqual(response.data, UNEXPECTED_ERROR_RESPONSE)




class TestOutboundSMS(TestCase):

    def setUp(self):
        User = get_user_model()
        user = User.objects.create(username='test_user1')
        user.set_password('12345')
        user.save()

        self.user = user
        token, _ = Token.objects.get_or_create(user=self.user)
        # print(token.user)
        self.valid_token = token.key
        self.invalid_token = 'this_invalid_token'

    def test_invalid_token_access_denied(self):
        """
        Testing bad auth, API request with invalid token
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.invalid_token)
        # print(client.__dict__)
        response = client.post('/outbound/sms/', OUTBOUND_VALID_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_token_access_success(self):
        """
        Testing good auth, API request with valid token
        """

        client = APIClient()
        authori = 'Token ' + self.valid_token
        client.credentials(HTTP_AUTHORIZATION=authori)
        response = client.post('/outbound/sms/', OUTBOUND_VALID_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_success_request(self):
        client = APIClient()
        authori = 'Token ' + self.valid_token
        client.credentials(HTTP_AUTHORIZATION=authori)
        response = client.post('/outbound/sms/', OUTBOUND_VALID_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OUTBOUND_VALID_RESPONSE)

    def test_variable_required_request(self):
        client = APIClient()
        authori = 'Token ' + self.valid_token
        client.credentials(HTTP_AUTHORIZATION=authori)
        response = client.post('/outbound/sms/', INVALID_DATA1, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, INVALID_DATA1_RESPONSE)

    def test_invalid_data_request(self):
        client = APIClient()
        authori = 'Token ' + self.valid_token
        client.credentials(HTTP_AUTHORIZATION=authori)
        response = client.post('/outbound/sms/', INVALID_DATA2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, INVALID_DATA2_RESPONSE)

    # def test_unexpected_error(self):
    #     client = APIClient()
    #     authori = 'Token ' + self.valid_token
    #     client.credentials(HTTP_AUTHORIZATION=authori)
    #     response = client.post('/outbound/sms/', INVALID_DATA1, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    #     self.assertEqual(response.data, UNEXPECTED_ERROR_RESPONSE)

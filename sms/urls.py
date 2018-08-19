from django.urls import path

from . import views


urlpatterns = [
    path('inbound/sms/', views.InboundSMS.as_view(), name='inbound_sms'),
    path('outbound/sms/', views.OutboundSMS.as_view(), name='outbound_sms'),
]
from django.core.cache import cache
from .serializers import InOutboundSMSSerializer


class InboundSmsHelper(object):

    def validate(self, data, *args, **kwargs):
        inbound_serializer = InOutboundSMSSerializer(data=data)
        inbound_serializer.is_valid(raise_exception=True)

class OutboundSmsHelper(object):

    def validate(self, data, *args, **kwargs):
        outbound_serializer = InOutboundSMSSerializer(data=data)
        outbound_serializer.is_valid(raise_exception=True)

class CacheHelper(object):

    def _get_key(self, data = {}):
        return data.get('from', '') + '_' + data.get('to')

    def set(self, data={}, timeout=14400, *args, **kwargs):
        text = data.get('text').strip()
        if text == 'STOP':
            cache.set(self._get_key(data=data), True, timeout)

    def get(self, data={}, *args, **kwargs):
        return cache.get(self._get_key(data=data), None)


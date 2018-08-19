from rest_framework import serializers

class InboundSMSSerializer(serializers.Serializer):

    from_ = serializers.CharField(required=True, min_length=6, max_length=16)
    to = serializers.CharField(required=True, min_length=6, max_length=16)
    text = serializers.CharField(required=True, min_length=1, max_length=120)


    def __init__(self, *args, **kwargs):
        super(InboundSMSSerializer, self).__init__(*args, **kwargs)
        self.fields['from'] = self.fields['from_']
        del self.fields['from_']

        # self.fields['from'].error_messages['required'] = 'from field is required'
        # self.fields['from'].error_messages['min_length'] = 'Minimum 6 length is required'



class OutboundSMSSerializer(serializers.Serializer):

    from_ = serializers.CharField(required=True, min_length=6, max_length=16)
    to = serializers.CharField(required=True, min_length=6, max_length=16)
    text = serializers.CharField(required=True, min_length=1, max_length=120)

    def __init__(self, *args, **kwargs):
        super(OutboundSMSSerializer, self).__init__(*args, **kwargs)
        self.fields['from'] = self.fields['from_']
        del self.fields['from_']

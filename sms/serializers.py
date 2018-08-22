from rest_framework import serializers


class InOutboundSMSSerializer(serializers.Serializer):

    from_ = serializers.CharField()
    to = serializers.CharField()
    text = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super(InOutboundSMSSerializer, self).__init__(*args, **kwargs)
        self.fields['from'] = self.fields['from_']
        del self.fields['from_']
        self.fields['from'].error_messages[
            'required'] = 'from is missing'
        self.fields['to'].error_messages[
            'required'] = 'to is missing'
        self.fields['text'].error_messages[
            'required'] = 'text is missing'

    def validate_to(self, to, *args, **kwargs):
        if len(to) < 6 or len(to) > 16:
            raise serializers.ValidationError("to is invalid")

    def validate_from(self, from_, *args, **kwargs):
        if len(from_) < 6 or len(from_) > 16:
            raise serializers.ValidationError("from is invalid")

    def validate_text(self, text, *args, **kwargs):
        if len(text) < 1 or len(text) > 120:
            raise serializers.ValidationError("text is invalid")


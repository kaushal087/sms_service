from rest_framework import serializers


class InboundSMSSerializer(serializers.Serializer):

    from_ = serializers.CharField()
    to = serializers.CharField()
    text = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super(InboundSMSSerializer, self).__init__(*args, **kwargs)
        self.fields['from'] = self.fields['from_']
        del self.fields['from_']
        self.fields['from'].error_messages[
            'required'] = 'from is missing'
        self.fields['to'].error_messages[
            'required'] = 'to is missing'
        self.fields['text'].error_messages[
            'required'] = 'text is missing'


    def validate_to(self, to, *args, **kwargs):
        if not to:
            raise serializers.ValidationError("to is missing")
        if len(to) < 6 or len(to) > 16:
            raise serializers.ValidationError("to is invalid")

    def validate_from(self, from_, *args, **kwargs):
        if not from_:
            raise serializers.ValidationError("from is missing")
        if len(from_) < 6 or len(from_) > 16:
            raise serializers.ValidationError("from is invalid")

    def validate_text(self, text, *args, **kwargs):
        if not text:
            raise serializers.ValidationError("text is missing")
        if len(text) < 1 or len(text) > 120:
            raise serializers.ValidationError("text is invalid")


class OutboundSMSSerializer(serializers.Serializer):

    from_ = serializers.CharField()
    to = serializers.CharField()
    text = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super(OutboundSMSSerializer, self).__init__(*args, **kwargs)
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


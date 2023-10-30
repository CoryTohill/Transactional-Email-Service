
from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    """
    Serialzier for email data to be sent to 3rd party service.
    """
    to_email = serializers.EmailField(required=True, help_text='The email address to send the email to.')
    to_name = serializers.CharField(required=True, help_text='The display name of the person to send the email to.')
    from_email = serializers.EmailField(required=True, help_text='The email address the email is sent from.')
    from_name = serializers.CharField(required=True, help_text='The display name of the person the email is sent from.')
    subject = serializers.CharField(required=True, help_text='The subject of the email.')
    body = serializers.CharField(required=True, help_text='The body of the email.')

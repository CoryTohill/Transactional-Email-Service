from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from transactional_email_service.serializers.email import EmailSerializer
from transactional_email_service.services.send_grid import send_email_via_sendgrid
from transactional_email_service.services.mailgun import send_email_via_mailgun
from django.conf import settings


@csrf_exempt
def send_email_view(request):
    """
    Endpoint for sending an email. The request body should be a JSON object with the following data structure:
    {
      "to_email": The email address to send the email to.
      "to_name": The display name of the person to send the email to.
      "from_email": The email address the email is sent from.
      "from_name": The display name of the person the email is sent from.
      "subject": The subject of the email.
      "body": The body of the email.
    }
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmailSerializer(data=data)
        if serializer.is_valid():
            if settings.EMAIL_SERVICE.lower() == 'send_grid':
                send_email_via_sendgrid(**serializer.validated_data)
                return JsonResponse(data, status=200)
            elif settings.EMAIL_SERVICE.lower() == 'mailgun':
                send_email_via_mailgun(**serializer.validated_data)
                return JsonResponse(data, status=200)
            else:
                # TODO: Add logging
                raise Exception(f'Email service is not defined. Email was not sent.')
        else:
            return JsonResponse(serializer.errors, status=400)

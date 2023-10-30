from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from transactional_email_service.serializers.email import EmailSerializer


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
          # TODO: Send the email data to 3rd party service for actual sending.
          return JsonResponse(data, status=200)
        return JsonResponse(serializer.errors, status=400)

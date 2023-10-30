import requests
import json
from transactional_email_service.settings import SEND_GRID_API_KEY
from transactional_email_service.services.utils import convert_html_to_plain_text


def _get_sendgrid_headers():
    """
    Format and return the headers for SendGrid API requests.
    Returns:
        Dictionary of SendGrid API request headers.
    """
    return {
        'Authorization': f'Bearer {SEND_GRID_API_KEY}',
        'Content-Type': 'application/json'
    }


def send_email_via_sendgrid(to_email, to_name, from_email, from_name, subject, body):
    """
    Sends an email via SendGrid.

    Args:
        to_email (str): Email address to send the email to (the recipient).
        to_name (str): Display name of the person to send the email to (the recipient).
        from_email (str): Email address the email is sent from (the sender).
        from_name (str): Display name of the person the email is sent from (the sender).
        subject (str): Subject of the email.
        body (str): Body of the email as an HTML string.

    Returns:
        Response object from SendGrid API.
    """
    plain_text_body = convert_html_to_plain_text(body)
    data = {
        "personalizations": [
            {
                "to": [
                    {
                        "email": to_email,
                        "name": to_name
                    }
                ],
                "subject": subject
            }
        ],
        "content": [
            {
                "type": "text/plain",
                "value": plain_text_body
            }
        ],
        "from": {
            "email": from_email,
            "name": from_name
        },
        "reply_to": {
            "email": from_email,
            "name": from_name
        }
    }
    json_data = json.dumps(data)
    try:
        headers = _get_sendgrid_headers()
        response = requests.post('https://api.sendgrid.com/v3/mail/send', headers=headers, data=json_data)
        return response
    except Exception as e:
        # TODO: Add logging.
        raise Exception(f'Error sending email via SendGrid: {e}')

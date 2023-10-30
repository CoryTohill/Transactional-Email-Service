import requests
from transactional_email_service.services.utils import convert_html_to_plain_text
from transactional_email_service.settings import MAILGUN_API_KEY, MAILGUN_DOMAIN_NAME


def _get_mailgun_auth():
    """
    Format and return the auth data for Mailgun API requests.
    Returns:
        Tuple of Mailgun API auth data.
    """
    return ("api", MAILGUN_API_KEY)


def send_email_via_mailgun(to_email, to_name, from_email, from_name, subject, body):
    """
    Sends an email via Mailgun.

    Args:
        to_email (str): Email address to send the email to (the recipient).
        to_name (str): Display name of the person to send the email to (the recipient). Currently unused due to Mailgun's free tier.
        from_email (str): Email address the email is sent from (the sender). Currently unused due to Mailgun's free tier.
        from_name (str): Display name of the person the email is sent from (the sender).
        subject (str): Subject of the email.
        body (str): Body of the email as an HTML string.

    Returns:
        Response object from Mailgun API.
    """
    auth_data = _get_mailgun_auth()
    plain_text_body = convert_html_to_plain_text(body)
    try:
        # TODO: Fully sign up for Mailgun to allow using from_email and to_name functionality.
        response = requests.post(
            f'https://api.mailgun.net/v3/{MAILGUN_DOMAIN_NAME}/messages',
            auth=auth_data,
            data={
                'from': f'{from_name} <mailgun@{MAILGUN_DOMAIN_NAME}>',
                'to': to_email,
                'subject': subject,
                'text': plain_text_body
            }
        )
        return response
    except Exception as e:
        # TODO: Add logging.
        raise Exception(f'Error sending email via Mailgun: {e}')

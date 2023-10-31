import json
from django.urls import reverse
from django.test import TestCase, override_settings
from django.test import Client
from rest_framework import status


class EmailAPITest(TestCase):
    email_data = {
        "to_email": "johndoe@test.com",
        "to_name": "John Doe",
        "from_email": "janedoe@test.com",
        "from_name": "Jane Doe",
        "subject": "New Bill",
        "body": "<h1>Your Bill</h1><p>$10</p>"
    }

    @override_settings(EMAIL_SERVICE='send_grid')
    def test_valid_send_grid_email(self):
        client = Client()
        response = client.post(
            reverse('email'),
            data=json.dumps(self.email_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.email_data)

    @override_settings(EMAIL_SERVICE='mailgun')
    def test_valid_mailgun_email(self):
        client = Client()
        response = client.post(
            reverse('email'),
            data=json.dumps(self.email_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.email_data)

    def test_all_fields_are_required(self):
        client = Client()
        response = client.post(
            reverse('email'),
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
            'to_email': ['This field is required.'],
            'to_name': ['This field is required.'],
            'from_email': ['This field is required.'],
            'from_name': ['This field is required.'],
            'subject': ['This field is required.'],
            'body': ['This field is required.']
        })

    def test_email_fields_must_be_emails(self):
        client = Client()
        data = self.email_data.copy()
        data['to_email'] = 'invalid_email'
        data['from_email'] = 'invalid_email'
        response = client.post(
            reverse('email'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
            'from_email': ['Enter a valid email address.'],
            'to_email': ['Enter a valid email address.']
        })

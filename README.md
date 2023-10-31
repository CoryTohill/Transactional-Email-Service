# Transactional-Email-Service
## Installation
### Clone the repo to your local machine
```
git clone git@github.com:CoryTohill/Transactional-Email-Service.git
```
Once cloned, you will need to navigate to the root of the project.


### Setup a virtual environment
You will want to set up a virtual environment locally if you don't have one already. For this project, I used pyenv to create a virtual environment and used Python version 3.11.3

[Pyenv Installation instructions](https://github.com/pyenv/pyenv#installation)

Once you have pyenv installed, you can download the correct Python version with the following:
```
pyenv install 3.11.3
```
And you can create your virtual environment with the correct python version using:
```
pyenv virtualenv 3.11.3 <your_env_name>
```
To activate your virtual environment, use:
```
pyenv activate <your_env_name>
```


### Pip Install
Once your virtual environment is set up and active, you will want to install the required packages using pip. If you do not have pip installed yet, you can install it by (following these instructions)[https://pip.pypa.io/en/stable/installation/]

To install the packages, run:
```
pip install -r requirements.txt
```

### Setup environment variables
There are a few environment variables that should be set before running the server locally. In your terminal where you will run the server, you can set the environment variables using the following command:
```
export ENV_VAR_NAME=value
```
You will need to set value for the following environment variables:
```
EMAIL_SERVICE
SENDGRID_API_KEY
MAILGUN_API_KEY
```
The `EMAIL_SERVICE` variable should be set to either `send_grid` or `mailgun`. This setting will determine which service will be used to actually send the email.

I did not include the API keys in the code for safety reasons since I will be making this repo public, but I will provide them via email.

### Run the server locally
To run the server locally, use the following command in your terminal from the root of the project:
```
python manage.py runserver
```

### Send requests locally
To send requests locally to the server, you will want to send a POST request to the endpoint `http://127.0.0.1:8000/email/`. The data should be JSON in the following format:
```
{
    "to_email": "johndoe@test.com",
    "to_name": "John Doe",
    "from_email": "janedoe@test.com",
    "from_name": "Jane Doe",
    "subject": "Check out this email",
    "body": "<h1>Hello Jane</h1><p>How are you?</p>"
}
```
You can either curl commands, or any service that you see fit to post the request. I personally use PostMan locally, which can be (downloaded here)[https://www.postman.com/downloads/].

### Running unit tests
To run unit tests, use the following commange from the root of the project:
```
python ./transactional_email_service/manage.py test ./transactional_email_service/transactional_email_service/tests
```

## Language, frameworks, and libraries used
I build this using Python 3.11.3, Django, Django Rest Framework (DRF), and the requests package. I wanted to write this using the latest version of Python, and chose to work with Django and the DRF due to both my familiarity with both packages and I wanted to show my familiarity with them. An alternative would have been to use something smaller like Flask since this service doesn't use a lot of the built in features of Django. I assumed while writing this that the code would ultimately be added to an existing Django project.

## Future work
If I continue to work on this project, the next thing I would do is to actually sign up SendGrid's and Mailgun's full services. It doesn't make a large difference when testing SendGrid at this stage, but Mailgun is limited in what you can do without fully signing up, mostly that you can only send an email from an address set up by them, and you can only send emails to up to 5 email accounts that you have to manually verify before you can send to them. If you need to have a test email verified, let me know and I can log in to set it up.

The second thing I would add is proper logging. I added some `# TODO:` comments in spots where logging should be added. I think it would be vital to have that so we could be aware of any service outtages from SendGrid or Mailgun immediately, allowing us to change the sending from one service to the other using the environment variables.

The third thing I'd add is a service like (Flagr)[https://github.com/openflagr/flagr], which allows you use and update feature flags in production without needed to restart the servers. I would then remove the `EMAIL_SERVICE` environment variable and use a feature flag instead. That would allow us to quickly change services without needing to restart servers should one of the services go down.


In total I spend about 4.5 hours on this project.

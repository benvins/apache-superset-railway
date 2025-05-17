import os
from flask_appbuilder.security.manager import AUTH_OAUTH

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

ENABLE_PROXY_FIX = True

SECRET_KEY = os.environ.get("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE")

# OAuth Configuration
AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True  # Set to True to allow users to self-register
AUTH_USER_REGISTRATION_ROLE = "Admin"  # Default role for new users

OAUTH_PROVIDERS = [
    {
        "name": "google",
        "icon": "fa-google",
        "token_key": "access_token",
        "remote_app": {
            "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
            "client_secret": os.environ.get("GOOGLE_SECRET"),  # Replace with your Client Secret
            "api_base_url": "https://www.googleapis.com/oauth2/v2/",
            "client_kwargs": {"scope": "email profile"},
            "request_token_url": None,
            "access_token_url": "https://accounts.google.com/o/oauth2/token",
            "authorize_url": "https://accounts.google.com/o/oauth2/auth",
            # If you want to restrict login to a specific domain:
            'whitelist': ['@benvins.com']
        },
    }
]
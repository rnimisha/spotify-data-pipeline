import base64
import logging

import requests

from airflow.exceptions import AirflowException
from config.appconfig import app_config


def token_from_authorization_code(authorization_code: str):
    """Generate token using authorization code"""

    CLIENT_ID = app_config.get_spotify_client_id()
    CLIENT_SECRET = app_config.get_spotify_client_secret()
    REDIRECT_URI = app_config.get_spotify_redirect_uri()
    url = "https://accounts.spotify.com/api/token"

    credentials = "%s:%s" % (CLIENT_ID, CLIENT_SECRET)

    base64_encoded = base64.b64encode(credentials.encode()).decode()
    logging.info("Retrieving access tokens........")
    response = requests.post(
        url,
        data={
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": REDIRECT_URI,
        },
        headers={"Authorization": "Basic " + base64_encoded},
    )
    logging.info("Access tokens retrieved........")
    response_json = response.json()
    access_token = response_json.get("access_token")

    return access_token


def get_access_token():
    """generates token if authorization code is present"""
    code = app_config.get_spotify_authorization_code()
    if code:
        access_token = token_from_authorization_code(authorization_code=code)
        return access_token
    else:
        logging.error("Authorization code is required")
        raise AirflowException("Authorization code is required")

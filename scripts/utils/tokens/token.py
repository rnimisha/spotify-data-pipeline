import base64

import requests

from airflow.exceptions import AirflowException
from config.appconfig import app_config

CLIENT_ID = app_config.get_spotify_client_id()
CLIENT_SECRET = app_config.get_spotify_client_secret()
REDIRECT_URI = app_config.get_spotify_redirect_uri()


def token_from_authorization_code(authorization_code: str):
    url = "https://accounts.spotify.com/api/token"
    credentials = "%s:%s" % (CLIENT_ID, CLIENT_SECRET)

    base64_encoded = base64.b64encode(credentials.encode()).decode()
    response = requests.post(
        url,
        data={
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": REDIRECT_URI,
        },
        headers={"Authorization": "Basic " + base64_encoded},
    )

    response_json = response.json()
    access_token = response_json.get("access_token")
    refresh_token = response_json.get("refresh_token")

    return access_token, refresh_token


def get_access_token():
    code = app_config.get_spotify_authorization_code()
    if code:
        access_token, refresh_token = token_from_authorization_code(
            authorization_code=code
        )
        print("Access Token: ", access_token)
        print("Refresh Token: ", refresh_token)
        return access_token
    else:
        raise AirflowException("Authorization code is required")

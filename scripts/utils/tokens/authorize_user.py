from airflow.exceptions import AirflowException
from config.appconfig import app_config
from scripts.utils.automation.login_handler import handle_login
from scripts.utils.automation.recaptcha_handler import handle_recaptcha
from scripts.utils.automation.web_driver import get_webdriver


def authorize_user() -> str:
    """_summary_
    Verifies user to generate authorization code
    Returns:
        str: spotify authorization code
    """
    try:
        SPOTIFY_CLIENT_ID = app_config.get_spotify_client_id()
        SPOTIFY_REDIRECT_URI = app_config.get_spotify_redirect_uri()
        scope = "user-read-recently-played"

        driver = get_webdriver()
        auth_url = f"https://accounts.spotify.com/authorize?client_id={SPOTIFY_CLIENT_ID}&response_type=code&redirect_uri={SPOTIFY_REDIRECT_URI}&scope={scope}"

        handle_login(driver, auth_url)

        if "recaptcha" in driver.current_url:
            handle_recaptcha(driver)

        current_url = driver.current_url
        authorization_code = current_url.split("code=")[1]

        # Close the browser
        driver.quit()

        print("..... authorization code ........", authorization_code)

        return authorization_code

    except Exception as e:
        raise AirflowException(f"Error in authentication process: ", e)

import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from airflow.exceptions import AirflowException
from config.appconfig import app_config


def handle_login(driver, auth_url):
    """Automates user login to spotify"""
    try:
        username = app_config.get_my_spotify_username()
        password = app_config.get_my_spotify_password()

        logging.info("Loging in to spotify.....")
        driver.get(auth_url)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-username"))
        )

        username_element = driver.find_element(By.ID, "login-username")
        password_element = driver.find_element(By.ID, "login-password")
        login_button = driver.find_element(By.ID, "login-button")

        username_element.send_keys(username)
        password_element.send_keys(password)

        login_button.click()
        logging.info("Logged in to spotify successfully")

    except Exception as e:
        logging.error(f"Error logging into spotify: {e}")
        raise AirflowException(f"Error logging into spotify: {e}")

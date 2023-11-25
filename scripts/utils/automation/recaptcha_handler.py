import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from airflow.exceptions import AirflowException


def handle_recaptcha(driver):
    """Solves recaptcha encountered in spotify login"""
    try:
        logging.info("Switching to reCAPTCHA iframe...")
        iframe = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        driver.switch_to.frame(iframe)
        print(driver.current_url)

        logging.info("Clicking reCAPTCHA checkbox...")
        checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "recaptcha-anchor"))
        )
        checkbox.click()

        logging.info(f"Current URL: {driver.current_url}")

        driver.switch_to.default_content()

        logging.info("Clicking continue button...")
        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@data-encore-id="buttonPrimary"]')
            )
        )
        continue_button.click()

        time.sleep(20)

        logging.info("Successfully handled reCAPTCHA.")

    except Exception as e:
        logging.error(f"Error occurred while solving reCAPTCHA: {e}")
        raise AirflowException(f"Error occurred while solving reCAPTCHA: {e}")

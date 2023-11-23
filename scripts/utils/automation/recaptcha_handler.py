import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def handle_recaptcha(driver):
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    # Recaptcha checkbox
    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "recaptcha-anchor"))
    )
    checkbox.click()

    driver.switch_to.default_content()

    continue_button = driver.find_element(
        By.XPATH, '//button[@data-encore-id="buttonPrimary"]'
    )
    continue_button.click()

    time.sleep(10)

    driver.refresh()

    current_url = driver.current_url

    # Wait for redirection to occur
    WebDriverWait(driver, 10).until(EC.url_changes(current_url))

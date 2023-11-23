import time

from selenium.webdriver.common.by import By

from config.appconfig import app_config


def handle_login(driver, auth_url):
    username = app_config.get_my_spotify_username()
    password = app_config.get_my_spotify_password()
    driver.get(auth_url)
    time.sleep(10)

    username_element = driver.find_element(By.ID, "login-username")
    password_element = driver.find_element(By.ID, "login-password")
    login_button = driver.find_element(By.ID, "login-button")

    username_element.send_keys(username)
    password_element.send_keys(password)

    login_button.click()

    time.sleep(10)

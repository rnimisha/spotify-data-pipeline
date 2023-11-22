from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_webdriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)
    return driver

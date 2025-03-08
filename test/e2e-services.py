import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def test_scores_service(url):
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub', options=options)

    try:
        driver.get(url)
        time.sleep(2)  # Wait for page to load

        score_element = driver.find_element(By.TAG_NAME, "h1")
        score_text = score_element.text.replace("The score is: ", "").strip()
        score = int(score_text)

        return 1 <= score <= 1000
    except Exception as e:
        print(f"Test failed: {e}")
        return False
    finally:
        driver.quit()


def main():
    url = "http://flask_app:5000"
    test_result = test_scores_service(url)
    sys.exit(0 if test_result else -1)


if __name__ == "__main__":
    main()
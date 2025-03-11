import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scores_service(url):
    """Test that the score is between 1 and 1000."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service("/usr/local/bin/chromedriver")
    service.start()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        score_text = driver.find_element(By.TAG_NAME, "h1").text.replace("The score is: ", "").strip()
        score = int(score_text)

        return 1 <= score <= 1000
    except Exception as e:
        print(f"Test failed: {e}")
        return False
    finally:
        driver.quit()
        service.stop()

def main():
    url = "http://localhost:8777"
    test_result = test_scores_service(url)
    sys.exit(0 if test_result else -1)

if __name__ == "__main__":
    main()

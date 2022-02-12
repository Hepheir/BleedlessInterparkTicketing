import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver


EXECUTABLE_PATH = os.path.abspath('drivers/chromedriver_mac64_m1-2')

driver: WebDriver


class DriverForWithStatement:
    def __enter__(self) -> WebDriver:
        return driver

    def __exit__(self, type, value, traceback) -> None:
        driver.quit()
        return


try:
    driver = webdriver.Chrome(EXECUTABLE_PATH)
except WebDriverException as webDriverException:
    # macOS 사용자의 경우.
    # 에러 메시지가 다음과 같다면, 아래의 방법을 시도해 볼 것.
    # selenium.common.exceptions.WebDriverException: Message: 'chromedriver_mac64_m1-2.zip' executable may have wrong permissions. Please see https://chromedriver.chromium.org/home
    # 컨트롤 키(⌃)를 누른채로 크롬드라이버 파일을 1회 실행시켜, 파일에 권환을 부여해볼것.
    raise webDriverException
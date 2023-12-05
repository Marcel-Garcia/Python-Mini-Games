import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Browser:
    browser, service = None, None

    # Initialise the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str):
        self.service = Service(driver)
        # self.browser = webdriver.Chrome(service=self.service)
        self.browser = webdriver.Edge(service=self.service )

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_qlik(self, username: str, password: str):
        self.add_input(by=By.CLASS_NAME, value='auth0-lock-input', text=username)
        self.add_input(by=By.CLASS_NAME, value='auth0-lock-input"', text=password)
        self.click_button(by=By.CLASS_NAME, value='auth0-label-submit')


if __name__ == '__main__':
    browser = Browser('drivers/edge')

    browser.open_page('https://login.qlik.com/login?state=hKFo2SAtWlZINmdheWg5d1VJSVg1Wk9lcmFKY1BkTEh6ZGdUOKFupWxvZ2luo3RpZNkgZmFHWmRCMmNJMmhTLTBIdWl4U3ZNMmtnZU1JekdJQlajY2lk2SB6YlNaVG8yVzRRVnpsTGhlVW9rNTVxWXZtOTJ3cGVEcw&client=zbSZTo2W4QVzlLheUok55qYvm92wpeDs&protocol=samlp&SAMLRequest=pVLLTuswEP0Vy%2FvGiZNeGqspKpQrKgVRSAqCneuaxpDYqe0Uytfj9AFhg5BYjufMnMd4ePpWlWDDtRFKJjDwfAi4ZGop5CqB8%2Fx%2FbwBPR0NDqxLXZNzYQt7ydcONBW5QGrLvJLDRkihqhCGSVtwQy0g2vkoJ9nxSa2UVUyUEY2O4to7qXEnTVFxnXG8E4%2FPbNIGFtbUhCDFVVY0UduutS%2FHiuRJRR4xaKlSqlZAQTJwCIandqT4O7npfQy2%2BRu%2BL7DFX%2BD66uXsv04LP1Uu%2Fv37YVDF%2BrfnEQDCdJJBGEV8Eob8MngYB85%2BjaED%2FFcEqiiNWhCcOZEzDp9JYKm0CsY%2FDnh%2F2cJwHIcEx6Q88H8ePEMwOXs%2BE3Gf4UzCLPciQyzyf9WbXWQ7B3fEWDgAPyZMdu%2B5G%2FvNieswZjn6T6hB1aT7PnTFVO3mtp7ftuWp2zuFnezqZpcLYbn0hrd6CVLE%2FH8VxbsSS6%2FY4rdPvayAaHTR3ZKDvsr8eut929AE%3D&RelayState=a21f6g18b80137ch2fidd81a4b6jj')
    time.sleep(3)

    browser.login_qlik(username='marcel.garciaorduna@***********', password='*************')
    time.sleep(10)

    browser.close_browser()
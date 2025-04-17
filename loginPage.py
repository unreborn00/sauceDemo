import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, credentials):
        self.driver = credentials.driver
        self.wait = credentials.wait
        self.username = credentials.username
        self.password = credentials.password
    def login_with_user(self, index=1):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))).send_keys(self.username[index])
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password"))).send_keys(self.password)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#login-button"))).click()
        self.driver.save_screenshot("failed_user_login.png")









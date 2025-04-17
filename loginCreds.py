from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class SauceDemo:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.username = []  # store usernames list
        self.password = ""

    def open_website(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
    def get_username(self):
        usernames = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#login_credentials")))
        self.username = usernames.text.replace("Accepted usernames are:", "").strip().split("\n")

    def get_password(self):
        passwords = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login_password")))
        self.password = passwords.text.replace("Password for all users:", "").strip()
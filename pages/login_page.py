from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_Page():
    def __init__ (self, driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)

    EMAIL_FIELD = (By.ID, 'email')
    PASS_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.btn-submit')




    def open(self):
        self.driver.get('https://practice.qabrains.com/')
        self.driver.maximize_window()
        
        
    def find_login_elements(self):
        self.email_box = self.wait.until(EC.presence_of_element_located(self.EMAIL_FIELD))
        self.pass_box = self.driver.find_element(*self.PASS_FIELD)
        self.login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        
    def login(self, email, password):
        email_input=self.wait.until(EC.presence_of_element_located(self.EMAIL_FIELD))
        email_input.send_keys(email)
        
        self.driver.find_element(*self.PASS_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
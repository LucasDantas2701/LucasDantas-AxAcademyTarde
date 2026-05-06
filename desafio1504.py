from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

URL = "http://automationexercise.com"

class User:
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.driver.get(URL)

    def find(self, selector, by=By.CSS_SELECTOR):
            EC.presence_of_element_located((by, selector))

    def click(self, selector, by=By.CSS_SELECTOR):
        element = self.find(selector, by)
        print(element.text)
        element.click()

    def type(self, selector, text, by=By.CSS_SELECTOR):
        element = self.find(selector, by)
        element.clear()
        element.send_keys(text)

    def select(self, selector, value, by=By.CSS_SELECTOR):
        element = self.find(selector, by)
        Select(element).select_by_visible_text(value)

user =User()
user.click('#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a')
user.type('#form > div > div > div:nth-child(3) > div > form > input[type=text]:nth-child(2)', 'lucas')
user.type('#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)', 'lucasdantas@email.com')
user.click('#form > div > div > div:nth-child(3) > div > form > button')
user.click('#id_gender1')
user.type('#password', '12345')
user.select('#days', '5')
user.select('#months', 'January')
user.select('#years', '2005')
user.click('#newsletter')
user.click('#optin')
user.type('#first_name', 'Lucas')
user.type('#last_name', 'Dantas')
user.type('#company', 'Dantas') 
user.type('#address1', 'Rua 1')
user.type('#address2', 'Rua 2')
user.click('#country')
user.click('#country > option:nth-child(2)')
user.type('#state', 'Rio de Janeiro')
user.select('#city', 'Rio de Janeiro')
user.type('#zipcode', '12345')
user.type('#mobile_number', '123456789')
from src.utils.web_functions import User #funções
from src.utils.constants.mock  import user_data
from src.modules.F_contact_form.mock import selectors, image 
from src.utils.constants.url import URL #url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

user = User(chrome)
chrome.get(URL)

user.click(selectors["btn_contact_us"])
user.type(selectors["username"], user_data['username'])
user.type(selectors["email"], user_data['email'])
user.type(selectors["subject"], 'Compra estornada')
user.type(selectors["message"], 'Estou com problemas ao comprar um produto')
user.send_files(selectors["attachment"], image)
user.click(selectors["submit"])
user.alert_accept()
time.sleep(5)
user.click(selectors["btn_home"])
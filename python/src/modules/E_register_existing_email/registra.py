from src.utils.web_functions import User #funções
from src.utils.constants.mock  import user_data
from src.modules.A_register_user.mockRegister import selectors
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

def registrar_user():
    user.click(selectors["btn_login_cadastro"])
    user.type(selectors["username_input"], user_data['username'])
    user.type(selectors["email_input"], user_data['email'])
    user.click(selectors["signup_button"])



    
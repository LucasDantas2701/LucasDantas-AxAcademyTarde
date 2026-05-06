from src.modules.X_register_dinamico.registra import registrar_user
from src.utils.web_functions import User #funções
from src.utils.constants.mock  import user_data
from src.shared.user_functions import login_user, delete_user
from src.utils.constants.mock  import register as selectors
from src.utils.constants.url import URL #url
from src.modules.A_register_user.registra import register_user
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome = webdriver.Chrome(
    service=Service(ChromeDriverManager().install(),)
    )
user = User(chrome)
chrome.get(URL)


Email = input("Email: ")

user.click(selectors["btn_login_cadastro"])
user.type(selectors["username_input"], user_data['username'])
user.type(selectors["email_input"], Email)
user.click(selectors["signup_button"])
time.sleep(2)

if  user.find(selectors["email_already_exists"]):
    login_user(user,Email)
    delete_user(user)
    register_user(user,Email)
    
else:
    registrar_user(user)
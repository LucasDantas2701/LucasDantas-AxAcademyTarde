from src.modules.E_register_existing_email.registra import registrar_user
from utils.web_functions import User #funções
from src.utils.constants.mock  import user_data, selectors
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
registrar_user(user)
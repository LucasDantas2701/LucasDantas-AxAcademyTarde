from src.utils.web_functions import User #funções
from src.utils.constants.mock  import selectors
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

time.sleep(3)
user.click(selectors["btn_test_cases"])
time.sleep(5)
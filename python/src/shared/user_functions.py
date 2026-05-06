from src.utils.web_functions import User #funções
from src.utils.constants.mock  import user_data, selectors #dados mockados
from src.utils.constants.url import URL #url
import time

def delete_user(user):
    user.click(selectors["btn_delete"])
    user.click(selectors["btn_confirm_delete"])
    print("Usuário deletado com sucesso")
    time.sleep(2)

def login_user(user,Email):
    user.click(selectors["btn_login_cadastro"])
    user.type(selectors["input_email"],Email)
    user.type(selectors["input_password"], user_data['password'])
    user.click(selectors["btn_login"])
    print('Usuário logado com sucesso')
    time.sleep(2)

def logout_user(user):
    login_user()
    user.click(selectors["btn_logout"])
    user.click(selectors["btn_home"])
    print('Usuário deslogado com sucesso')
    time.sleep(2)
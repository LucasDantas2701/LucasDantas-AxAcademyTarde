from src.utils.constants.mock  import user_data
from src.utils.constants.mock  import register as selectors

def registrar_user(user):
    user.click(selectors["gender_radio"])
    user.type(selectors["password_input"], user_data['password'])
    user.selectDropDOWN(selectors["birth_day_select"], user_data['birth_day'])
    user.selectDropDOWN(selectors["birth_month_select"], user_data['birth_month'])
    user.selectDropDOWN(selectors["birth_year_select"], user_data['birth_year'])
    user.click(selectors["newsletter_checkbox"])
    user.click(selectors["optin_checkbox"])
    user.type(selectors["first_name_input"], user_data['first_name'])
    user.type(selectors["last_name_input"], user_data['last_name'])
    user.type(selectors["company_input"], user_data['company'])
    user.type(selectors["address1_input"], user_data['address1'])
    user.type(selectors["address2_input"], user_data['address2'])
    user.click(selectors["country_dropdown"])
    user.click(selectors["country_option_2"])
    user.type(selectors["state_input"], user_data['state'])
    user.type(selectors["city_input"], user_data['city'])
    user.type(selectors["zipcode_input"], user_data['zipcode'])
    user.type(selectors["mobile_input"], user_data['mobile'])
    user.click(selectors["create_account_button"])
    user.click(selectors["continue_button"])
    print('Usuário registrado com sucesso')


    
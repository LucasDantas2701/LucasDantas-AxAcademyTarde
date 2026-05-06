user_data = {
    "username": "lucas",
    "email": "lucasdantas13@email.com",
    "wrongPassword": "1234",
    "password": "12345",
    "birth_day": "5",
    "birth_month": "January",
    "birth_year": "2005",
    "newsletter": True,
    "optin": True,
    "first_name": "Lucas",
    "last_name": "Dantas",
    "company": "fpf",
    "address1": "Rua 1",
    "address2": "Rua 2",
    "country": "India",
    "state": "Rio de Janeiro",
    "city": "Rio de Janeiro",
    "zipcode": "12345",
    "mobile": "123456789"
}
selectors = {
    "btn_login_cadastro": "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a",  # botão login/cadastro
    "input_email": "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=email]:nth-child(2)",  # campo de email
    "input_password": "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=password]:nth-child(3)",  # campo de senha
    "btn_login": "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > button",  # botão de login
    "btn_delete": "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a",  # botão deletar usuário
    "btn_confirm_delete": "#form > div > div > div > div > a",  # botão confirmar exclusão
    "btn_logout": "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a",  # botão logout
    "btn_home" : "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(1) > a", #botao home,
    "btn_contact_us" : "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(8) > a", #botao contato
    "btn_test_cases" : "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a"
}
register = {
    "btn_login_cadastro": "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a",  # botão login/cadastro
    "username_input": "#form > div > div > div:nth-child(3) > div > form > input[type=text]:nth-child(2)",
    "email_already_exists": "#form > div > div > div:nth-child(3) > div > form > p",
    "email_input": "#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)",
    "signup_button": "#form > div > div > div:nth-child(3) > div > form > button",
    "gender_radio": "#id_gender1",
    "password_input": "#password",
    "birth_day_select": "#days",
    "birth_month_select": "#months",
    "birth_year_select": "#years",
    "newsletter_checkbox": "#newsletter",
    "optin_checkbox": "#optin",
    "first_name_input": "#first_name",
    "last_name_input": "#last_name",
    "company_input": "#company",
    "address1_input": "#address1",
    "address2_input": "#address2",
    "country_dropdown": "#country",
    "country_option_2": "#country > option:nth-child(2)",
    "state_input": "#state",
    "city_input": "#city",
    "zipcode_input": "#zipcode",
    "mobile_input": "#mobile_number",
    "create_account_button": "#form > div > div > div > div.login-form > form > button",
    "continue_button": "#form > div > div > div > div > a"
}
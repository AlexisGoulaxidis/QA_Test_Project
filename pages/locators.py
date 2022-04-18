from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
class LoginPageLocators():
    LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.XPATH, '//div[@class="col-sm-6 login_form"]')
    REGISTER_FORM = (By.XPATH, '//div[@class="col-sm-6 register_form"]')
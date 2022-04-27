from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
class LoginPageLocators():

    LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.XPATH, '//div[@class="col-sm-6 login_form"]')
    LOGIN_EMAIL_INPUT = (By.XPATH, '//input[@id="id_login-username"]')
    LOGIN_PASSWORD_INPUT = (By.XPATH, '//input[@id="id_login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')
    
    REGISTER_FORM = (By.XPATH, '//div[@class="col-sm-6 register_form"]')
    REGISTER_EMAIL_INPUT = (By.XPATH, '//input[@id="id_registration-email"]')
    REGISTER_PASSWORD_1_INPUT = (By.XPATH, '//input[@id="id_registration-password1"]')
    REGISTER_PASSWORD_2_INPUT = (By.XPATH, '//input[@id="id_registration-password2"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
    
    
    
class BasketPageLocators():

    BASKET_LINK = 'http://selenium1py.pythonanywhere.com/ru/basket/'
    BASKET_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    BASKET_ITEMS = (By.XPATH, '//div[@class="basket-items"]')
    BASKET_EMPTY_TEXT = (By.XPATH, '//div[@id="content_inner"]/p')
    
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    PRODUCT_ADDED_TEXT = (By.XPATH, '//div[@class="alertinner "]/strong')
    PRODUCT_ADDED_PRICE_TEXT = (By.XPATH, '//div[@class="alertinner "]/p/strong')
    
    
class BasePageLocators():

    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    LOGIN_LINK_INVALID = (By.XPATH, '//a[@id="login_link_inc"]')
    BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default" and contains(@href, "/basket/")]')
    
    LOGOUT_BUTTON = (By.XPATH, "//a[@id='logout_link']")
    
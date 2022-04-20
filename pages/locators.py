from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    
class LoginPageLocators():
    LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.XPATH, '//div[@class="col-sm-6 login_form"]')
    REGISTER_FORM = (By.XPATH, '//div[@class="col-sm-6 register_form"]')
    
class BasketPageLocators():
   BASKET_LINK = 'http://selenium1py.pythonanywhere.com/ru/basket/'
   BASKET_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
   PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
   PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
   PRODUCT_ADDED_TEXT = (By.XPATH, '//div[@class="alertinner "]/strong')
   PRODUCT_ADDED_PRICE_TEXT = (By.XPATH, '//div[@class="alertinner "]/p/strong')
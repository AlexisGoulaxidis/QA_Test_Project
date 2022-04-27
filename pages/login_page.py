from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self): #contains the base class
    
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
    	
        assert self.browser.current_url == LoginPageLocators.LOGIN_LINK , f'{self.browser.current_url}'

    def should_be_login_form(self):
    
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'LOGIN FORM IS INCORRECT!'
        
    def should_be_register_form(self):
    
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'REGISTER FORM IS INCORRECT!'
        
    def register_new_user(self, email, password):
    
    	self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
    	self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1_INPUT).send_keys(password)
    	self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2_INPUT).send_keys(password)
    	self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
    	
    def login_user(self, email = 'jorno114433@gmail.com', password = 'itsNotMyProblemItsYours'): 
    
    	self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT).send_keys(email)
    	self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
    	self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
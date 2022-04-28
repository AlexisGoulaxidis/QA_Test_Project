from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class BasketPage(BasePage):


	#first create check and get name/price functions
	def get_item_name(self):
	
		assert self.is_element_present(*BasketPageLocators.PRODUCT_NAME), \
			'Item name is not presented'
		return self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
		
		
	def get_item_price(self):
	
		assert self.is_element_present(*BasketPageLocators.PRODUCT_PRICE), \
		        "Item price is not presented"
		
		return self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text
		
		
	def add_item_to_basket(self):
		
		self.product_name = self.get_item_name()
		self.product_price = self.get_item_price()
		self.browser.find_element(*BasketPageLocators.BASKET_BUTTON).click()
		
	def solve_quiz_and_get_code(self):
		
		self.wait.until(EC.alert_is_present())
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		time.sleep(2)
		try:
		
			self.wait.until(EC.alert_is_present())
			alert = self.browser.switch_to.alert
			print(f'Your code: {alert.text}')
			alert.accept()
		except NoAlertPresentException:
		
			print('\nNo second Alert presented\n')

	def should_be_item_added_to_basket_msg(self):
	
		added_product_text = self.browser.find_element(*BasketPageLocators.PRODUCT_ADDED_TEXT).text
		
		assert self.product_name == added_product_text, \
                f'Something wrong with the product name! Name in previus page = {self.product_name}, but in basket {added_product_text}'
		
	def should_be_item_price_correct_in_basket(self):
	
		added_product_price = self.browser.find_element(*BasketPageLocators.PRODUCT_ADDED_PRICE_TEXT).text
		
		assert self.product_price == added_product_price, \
		f'Something wrong with the price! Price in previus page = {self.product_cost}, but in basket {added_product_price}'
		
	def should_not_be_success_message(self):  #and price
	
		assert self.not_element_present(*BasketPageLocators.PRODUCT_ADDED_TEXT), \
		'\nADDED_TEXT MESSAGE IS BEFORE THE PURCHASE PROCESS\n'
		assert self.not_element_present(*BasketPageLocators.PRODUCT_ADDED_PRICE_TEXT), \
		'\nADDED_PRICE_TEXT MESSAGE IS BEFORE THE PURCHASE PROCESS\n'
		
	
	def should_not_be_disappeared_message(self):
	
		assert self.is_disappeared(*BasketPageLocators.PRODUCT_ADDED_TEXT), \
		'\nPRODUCT_ADDED_TEXT Is disappeared!\n'
		
	

from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):

	def should_not_be_items_in_basket(self):
		
		assert self.not_element_present(*CartPageLocators.BASKET_ITEMS), \
		'\n BASKET ITEMS IS PRESENTED! IT SHOULD\'T BE! \n'
	
	def should_be_text_about_empty_basket(self):
		
		assert self.is_element_present(*CartPageLocators.BASKET_EMPTY_TEXT), \
		'\n BASKET IS NOT EMPTY!\n'
			

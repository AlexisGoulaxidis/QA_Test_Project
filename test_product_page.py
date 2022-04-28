import pytest
from .pages.product_page import BasketPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
from random import randrange
import time



@pytest.mark.need_review
@pytest.mark.parametrize('promo', ["?promo=newYear2019",
                                   # "?promo=offer0",
                                   # "?promo=offer1",
                                   # "?promo=offer2",
                                   # "?promo=offer3",              #cart_page.py
                                   # "?promo=offer4",
                                   # "?promo=offer5",
                                   # "?promo=offer6",
                                   pytest.param("?promo=offer7",
                                                marks=pytest.mark.xfail(reason="We are working on that!")),
                                   # "?promo=offer8",
                                   #"?promo=offer9"
                                   ])
def test_guest_can_add_product_to_basket(browser,promo):
	
	try:
		browser.delete_all_cookies()
		link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/{promo}'
		page = BasketPage(browser, link)
		page.open()
		page.should_not_be_success_message()  #test_guest_cant_see_success_message_and_price
		page.add_item_to_basket()
		page.solve_quiz_and_get_code()
		page.should_be_item_added_to_basket_msg()
		page.should_be_item_price_correct_in_basket()
	
	
	except:
		raise AssertionError
		print(f'Problem at this link: {link}')


@pytest.mark.smoke
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

	browser.delete_all_cookies()
	
	link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
	page = BasketPage(browser, link)
	page.open()
	page.add_item_to_basket()
	page.should_not_be_success_message()  #test_guest_cant_see_success_message_and_price
		
@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):

	browser.delete_all_cookies()
	
	link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
	page = BasketPage(browser, link)
	page.open()
	page.should_not_be_success_message()  #test_guest_cant_see_success_message_and_price
	

@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser):

	browser.delete_all_cookies()

	link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
	page = BasketPage(browser, link)
	page.open()
	page.add_item_to_basket()
	page.solve_quiz_and_get_code()
	page.should_not_be_disappeared_message()  #test_guest_cant_see_success_message_and_price

	
@pytest.mark.regression
def test_guest_should_see_login_link_on_product_page(browser):

	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = BasketPage(browser, link)
	page.open()
	page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):

	link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
	page = BasketPage(browser, link)
	page.open()
	page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

	browser.delete_all_cookies()
	
	link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
	page = CartPage(browser, link)
	page.open()
	page.go_to_basket_page()
	page.should_not_be_items_in_basket()
	page.should_be_text_about_empty_basket()


class TestUserAddToBasketFromProductPage():


	@pytest.fixture(scope='function', autouse=True)
	def setup(self, browser):
	
		link = 'http://selenium1py.pythonanywhere.com/ru'
		page = LoginPage(browser, link)
		page.open()
		rand_password = str(time.time())
		rand_email = rand_password + "@randmail.org"
		page.go_to_login_page()
		page.register_new_user(rand_email, rand_password)
		page.should_be_authorized_user()
		
	
	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		
		try:
			link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
			page = BasketPage(browser, link)
			page.open()
			page.add_item_to_basket()
			page.should_be_item_added_to_basket_msg()
			page.should_be_item_price_correct_in_basket()
		
		
		except:
		
			print(f'Problem at this link: {link}')
			raise AssertionError
			



	def test_user_cant_see_success_message(self, browser):
		
		link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
		page = BasketPage(browser, link)
		page.open()
		page.should_not_be_success_message()  #test_guest_cant_see_success_message_and_price
		

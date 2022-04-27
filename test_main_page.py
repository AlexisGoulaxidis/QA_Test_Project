import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():

	def test_guest_can_go_to_login_page(browser):

	    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
	    page = MainPage(browser, link)
	    page.open()
	    login_page = page.go_to_login_page()
	    login_page.should_be_login_page()
	    
	def test_guest_should_see_login_link(browser):

	    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
	    page = LoginPage(browser, link)
	    page.open()
	    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    link = 'http://selenium1py.pythonanywhere.com/ru/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_items_in_basket()
    page.should_be_text_about_empty_basket()
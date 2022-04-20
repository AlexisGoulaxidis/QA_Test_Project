from .pages.product_page import BasketPage



def test_guest_can_add_product_to_basket(browser):
	
	link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
	page = BasketPage(browser, link)
	page.open()
	page.add_item_in_basket()
	page.solve_quiz_and_get_code()
	page.should_be_item_added_to_basket_msg()
	page.should_be_item_price_correct_in_basket()
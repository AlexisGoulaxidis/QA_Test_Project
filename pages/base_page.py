#first stage

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)
		self.wait = WebDriverWait(browser, 15)
	def open(self):
		self.browser.get(self.url)
	def is_element_present(self, how, what):   #get NoSuchElement
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException:
			return False
		return True
#this is config file for pytest fixtures to remember automaticaly in all tests in this directory 

import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome.options import Options
import time

#link for WebDriverManager guide https://github.com/SergeyPirogov/webdriver_manager

def pytest_addoption(parser):  #make command for selectd file (name of test)
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: opera or firefox", choices=('opera', 'firefox'))
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language', choices=('en', 'ru', 'fr'))
    
#pytest -s -v --browser_name=" " --language=" "  test.py  / the way to change browser/language when testing, but browser needs to be installed         


@pytest.fixture(scope="session", autouse=True) #if wanna target on function/class/method/session
def browser(request):
	
	browser_name = request.config.getoption("browser_name")  # Request get param from CMD
	user_language = request.config.getoption("language")
	
	#starting
	print('\n Start Browser for test')
	
	if browser_name == 'firefox':
		print('\n Starting Firefox')
		fp = webdriver.FirefoxProfile()
		#set language option
		fp.set_preference("intl.accept_languages", user_language)
		browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=fp)
		#Create Pref Options for language in browser in param accept_languages
			
	elif browser_name == 'opera':
		print('\n Starting Opera')
		options = Options()
		#set language option
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		browser = webdriver.Opera(executable_path=OperaDriverManager().install(),options=options)
	else:
		raise pytest.UsageError("--browser_name should be opera or firefox")
		
	yield browser 
		#last step of fixture
	print('\n Quit browser..')
	time.sleep(2)
	browser.close()
	browser.quit()
		
		
		
		
	

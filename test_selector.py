from selenium import webdriver
import time
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
browser = webdriver.Opera(executable_path=OperaDriverManager().install(),options=options)


try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)
    #first input
    browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]').send_keys('something')
    #second input
    browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]').send_keys('something')
    browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]').send_keys('something')
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

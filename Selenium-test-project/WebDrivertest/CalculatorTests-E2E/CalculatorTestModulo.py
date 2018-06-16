from selenium import webdriver
import time
import selenium.webdriver.support.ui as UI

driver = webdriver.Chrome()
# Open the desired web page
driver.get('http://juliemr.github.io/protractor-demo/')

first_number = driver.find_element_by_css_selector('[ng-model=first]')
first_number.send_keys('10')
second_number = driver.find_element_by_css_selector('[ng-model=second]')
second_number.send_keys('80')


operation_add = UI.Select(driver.find_element_by_css_selector('[ng-model=operator]')).select_by_value("MODULO")


result_button = driver.find_element_by_class_name('btn')
result_button.click()


time.sleep(4)
result = driver.find_element_by_class_name('ng-binding')


assert result.text == '10'
driver.quit()
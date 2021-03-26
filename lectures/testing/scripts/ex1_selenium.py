from selenium import webdriver
import requests


URL = "https://tsn.ua/"
# requests.get(URL)

driver = webdriver.Chrome()
driver.get(URL)

login_button = driver.find_element_by_id("btnSignIn")
print(login_button)
login_button.click()

sign_up_button = driver.find_element_by_id("btnSignUp")
sign_up_button.click()
input_name = driver.find_element_by_css_selector("input.f-control")
print(input_name)
input_name.click()
input_name.send_keys("Misha")
# re = requests.get(URL)
# print(re.text)

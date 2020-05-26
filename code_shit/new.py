from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.get("http://aduser.zdravnsk.ru/ad/login.php")


# Ввод логина
login = driver.find_element_by_name('login')
login.clear()
login.send_keys("tdv@nso.ru")

# Ввод пароля
pswd = driver.find_element_by_name("password")
pswd.clear()
pswd.send_keys("pass")

content = driver.find_element_by_class_name('login-button')
content.click()

driver.quit()
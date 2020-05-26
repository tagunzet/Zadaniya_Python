from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://svod.zdravnsk.ru/Login")

content = driver.find_element_by_class_name('login-button')
content.click()




login = driver.find_element_by_name('Login')
login.clear()
login.send_keys("tugunov")


password = driver.find_element_by_name('Password')

password.clear()
password.send_keys("123456")

driver.find_element_by_xpath("//button[@id='ext-gen55']").click()



xpatch = '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]'

xpatch2 = "//*[@id='shortcuts-item-2']"

xp = driver.find_element_by_class_name('item shortcutItem')
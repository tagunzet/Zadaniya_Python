from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select





#////////////////////////////////////////////////////
#Список переменных
login = ''
password =''
print('Выберете тип инциндента'+'\n',
      '\n + 1.Заявка на обслуживание',
        '\n + 2.Инцидент',
            '\n + 3.Заявка на консультацию',
                '\n + 4.Заявка на изменение')
print('Ответ : ')
tip = input ()
print('выберете тип приоритета'+'\n',
      '\n + 1.Неотложный',
        '\n + 2.Нормальный',
            '\n + 3.Высокий', )
print('Ответ : ')
prioritet = input()


print ('Тема тикета')
thememes = input()
print ('Тикет')
ticketmessages = input()




#////////////////////////////////////////////////////

driver = webdriver.Chrome()
driver.get("https://help.bars.group/index.php?/Base/User/Login")




# Ввод логина
login = driver.find_element_by_name('scemail')
login.clear()
login.send_keys("tdv@nso.ru")

# Ввод пароля
pswd = driver.find_element_by_name("scpassword")
pswd.clear()
pswd.send_keys("sosochek322")

content = driver.find_element_by_class_name('rebutton')
content.click()


hreff = driver.find_element_by_link_text("Отправить заявку").click()

driver.find_element_by_xpath("//input[@id='department_300']").click() #выбор 300 колонку
driver.find_element_by_xpath("//input[@id='department_301']").click() #выбор 301 департамент


content3 = driver.find_element_by_class_name('rebuttonwide2')
content3.click()


##Создание тикета ##########################################################\\

select = Select(driver.find_element_by_class_name('swiftselect'))
## Тут вначале запихать переменную тип обращения
select.select_by_visible_text(tip)
#select.select_by_visible_text('Заявка на изменение')
#select.select_by_visible_text('Инцидент')
#select.select_by_visible_text('Заявка на обслуживание')

select2 = Select(driver.find_element_by_name('ticketpriorityid'))
select2.select_by_visible_text(prioritet)
# select2.select_by_visible_text('Нормальный')
# select2.select_by_visible_text('Высокий')

select3 = Select(driver.find_element_by_name('g0d83djpn6gf'))

select4 = Select(driver.find_element_by_name('q4jhm4hmgfjs[0]'))
select4.select_by_visible_text('Новосибирск')

themeticket= driver.find_element_by_name('ticketsubject')
themeticket.send_keys(thememes)

messageticket= driver.find_element_by_name('ticketmessage')
messageticket.send_keys(ticketmessages)


##\#############################################################################//

#print(driver)


# from bs4 import BeautifulSoup as bs
# pr = driver.page_source
# soup = bs(pr)
# print(soup.prettify())

#Для того что бы отправилось нужно раскоментировать ниже две строки
#content6 = driver.find_element_by_class_name('rebuttonwide2')
#content6.click()
print('Данные введены')
print('Ожидается отправка')
#driver.quit()
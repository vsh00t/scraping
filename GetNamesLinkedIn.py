#!/usr/bin/env python3

from posixpath import split
import time
from tkinter.font import names
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


# This function iteratively clicks on the "Next" button at the bottom right of the search page.
def profiles_loop():
  actions = ActionChains(driver)
  # Cambiar el 10 por las veces que deseas que baje el scroll para que cargue mas perfiles
  for _ in range(10):
    actions.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(0.5)


def repeat_fun(times, f):
    for i in range(times): f()

def createFile(nombres):
    fp = open('results.csv', 'w')
    fp.write(nombres)
    fp.close()

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element(By.XPATH, '//*[@id="session_key"]')


# send_keys() to simulate key strokes
username.send_keys('<CORREO LINKEDIN>')
sleep(0.5)

# locate password form by_class_name
password = driver.find_element(By.XPATH,'//*[@id="session_password"]')

# send_keys() to simulate key strokes
password.send_keys('<PASSWORD LINKEDIN>')
sleep(0.5)

# locate submit button by_class_name
log_in_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')

# .click() to mimic button click
log_in_button.click()
sleep(0.5)

# locate search form by_name
search_query = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')

# send_keys() to simulate the search text key strokes
search_query.send_keys('<NOMBRE DE LA EMPRESA EN LINKEDIN>')

# .send_keys() to simulate the return key
search_query.send_keys(Keys.RETURN)
sleep(2)

goto_page_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/div/a/div/div[2]/div[2]/a')
goto_page_button.click()
sleep(3)

goto_people_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/nav/ul/li[5]/a')
goto_people_button.click()
sleep(3)


profiles_loop()
soup = BeautifulSoup(driver.page_source,'lxml')
result_div = soup.find_all('div', attrs={'class': 'org-people-profile-card__profile-title t-black lt-line-clamp lt-line-clamp--single-line ember-view'})

result = []
resultFinal = []
nombres = []
i=0
for x in result_div:
    result.append(str(x))
    preresult = (result[i].split('>'))
    nombre = (preresult[1])
    resultFinal.append(((nombre.split('<')[0]).rstrip()).lstrip())
    createFile(str(resultFinal))
    i=i+1

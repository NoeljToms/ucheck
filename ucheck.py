from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

USERNAME = ''
PASSWORD = ''
PATH = 'C:\Program Files (x86)\chromedriver.exe'

options = webdriver.ChromeOptions('headless')

driver = webdriver.Chrome(PATH, options=options)
driver.get('https://ucheck.utoronto.ca/')
driver.implicitly_wait(5)

#Logging in
username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
username.send_keys(USERNAME)
password.send_keys(PASSWORD + Keys.ENTER)
#driver.implicitly_wait(5) #Wait 5 seconds for webpage to load

#Filling out screening
start_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/button')

webdriver.ActionChains(driver).move_to_element(start_btn).perform()
webdriver.ActionChains(driver).double_click(start_btn).perform()

q1 = driver.find_element(By.XPATH, '//*[@id="f5d87fa4-41c1-41bf-9307-2eb2e7862a28-noFocus"]/fieldset/label[2]')
webdriver.ActionChains(driver).move_to_element(q1).perform()
webdriver.ActionChains(driver).double_click(q1).perform()
driver.implicitly_wait(0.5)
q2 = driver.find_element(By.XPATH, '//*[@id="ebdd2acd-87ff-47aa-a7d2-059677987580-noFocus"]/fieldset/label[1]')
webdriver.ActionChains(driver).move_to_element(q2).perform()
webdriver.ActionChains(driver).double_click(q2).perform()
driver.implicitly_wait(0.5)
q3 = driver.find_element(By.XPATH, '//*[@id="5c2a5703-ce69-40aa-bf5a-5ddd81335aa9-noFocus"]/fieldset/label[1]')
webdriver.ActionChains(driver).move_to_element(q3).perform()
webdriver.ActionChains(driver).double_click(q3).perform()
driver.implicitly_wait(0.5)
q4 = driver.find_element(By.XPATH, '//*[@id="296a215c-8f44-4ca0-b2bc-6861ddabec3b-noFocus"]/fieldset/label[1]')
webdriver.ActionChains(driver).move_to_element(q4).perform()
webdriver.ActionChains(driver).double_click(q4).perform()
driver.implicitly_wait(0.5)
q5 = driver.find_element(By.XPATH, '//*[@id="c2a1ba3f-0113-49a6-95cc-aeede171963a-noFocus"]/fieldset/label[1]')
webdriver.ActionChains(driver).move_to_element(q5).perform()
webdriver.ActionChains(driver).double_click(q5).perform()
driver.implicitly_wait(0.5)
q6 = driver.find_element(By.XPATH, '//*[@id="11985099-8548-4dc6-944f-bb4ea9c9494b-noFocus"]/fieldset/label[1]')
webdriver.ActionChains(driver).move_to_element(q6).perform()
webdriver.ActionChains(driver).double_click(q6).perform()
driver.implicitly_wait(0.5)
q7 = driver.find_element(By.XPATH, '//*[@id="801d8c6a-6523-437e-bb6d-fa4092dacab1-noFocus"]/fieldset/label[1]')
webdriver.ActionChains(driver).move_to_element(q7).perform()
webdriver.ActionChains(driver).double_click(q7).perform()
submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/main/div/div/div/div/div/button')
webdriver.ActionChains(driver).move_to_element(submit).perform()
webdriver.ActionChains(driver).double_click(submit).perform()
'''
Created on 26 May 2025

@author: Sandeep
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

'''1.Launching the Chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Creating an Object from ActionChains class'''
actions = ActionChains(driver)

'''4. Copying Text from Field1'''
'''Ctrl+a'''
field1_txt_bx = driver.find_element(By.ID, 'field1')
actions.key_down(Keys.CONTROL, field1_txt_bx).send_keys('a').key_up(Keys.CONTROL).perform()

''' Ctrl+c'''
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

'''5. Pasting Text to Field2'''
'''Ctrl+v'''
field2_txt_bx = driver.find_element(By.ID, 'field2')
actions.key_down(Keys.CONTROL, field2_txt_bx).send_keys('v').key_up(Keys.CONTROL).perform()













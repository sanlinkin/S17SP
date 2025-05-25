'''
Created on 25 May 2025

@author: Sandeep
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

'''1.Launching the Chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)


'''2. Creating an Object from ActionChains class'''
actions = ActionChains(driver)

'''3. Navigating to practice site'''
driver.get('https://demo.automationtesting.in/Resizable.html')

'''4. Resizable'''
source = driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
actions.drag_and_drop_by_offset(source, 150, 100).perform()




#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time 
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common import action_chains
#
#
# ''' Launching the chrome browser'''
#
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options)
# # driver = Chrome()
# driver.implicitly_wait(10)
#
#
# '''object creation'''
# actions = ActionChains(driver)
#
#
# ''' Navigating to practice site'''
# driver.get('https://demo.automationtesting.in/Resizable.html')
#
#
# '''re siez'''
#
# source = driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
# actions.drag_and_drop_by_offset(source, 250, 145).perform()





'''
Created on 23 May 2025

@author: Sandeep
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''1.Launching the Chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Simple Alert'''

'''clicking on Simple Alert Button'''
simple_alert_btn = driver.find_element(By.ID, 'alertBtn')
simple_alert_btn.click()

'''Switch to simple alert'''
simple_alert = driver.switch_to.alert

'''Printing the text on simple alert'''
simple_alert_text = simple_alert.text
print(simple_alert_text)
time.sleep(3)

'''Accepting the Simple Alert/Clicking OK on simple Alert'''
simple_alert.accept()










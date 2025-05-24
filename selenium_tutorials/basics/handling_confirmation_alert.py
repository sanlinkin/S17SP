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

'''3. Confirmation Alert'''
'''clicking on confirmation Alert Button'''
confirmation_alert_btn = driver.find_element(By.ID, 'confirmBtn')
confirmation_alert_btn.click()

'''Switch to confirmation alert'''
confirmation_alert = driver.switch_to.alert

'''Printing the text on confirmation alert'''
confirmation_alert_text = confirmation_alert.text
print(confirmation_alert_text)
time.sleep(5)

'''Accepting the confirmation Alert/Clicking OK on confirmation Alert'''
confirmation_alert.accept()













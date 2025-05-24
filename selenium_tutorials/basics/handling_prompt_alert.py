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

'''3. Prompt Alert'''
'''clicking on Prompt Alert Button'''
prompt_alert_btn = driver.find_element(By.ID, 'promptBtn')
prompt_alert_btn.click()

'''Switch to Prompt Alert'''
prompt_alert = driver.switch_to.alert

'''Printing the text on Prompt alert'''
prompt_alert_text = prompt_alert.text
print(prompt_alert_text)
time.sleep(3)

'''Accepting the Prompt Alert/Clicking OK on Prompt Alert'''
prompt_alert.send_keys("neymar")
prompt_alert.accept()











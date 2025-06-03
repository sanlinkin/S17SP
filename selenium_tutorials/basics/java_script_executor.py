'''
Created on 3 Jun 2025

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

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Enter date in Date picker2'''
driver.execute_script('document.getElementById("txtDate").removeAttribute("readonly")')

date_picker_2 = driver.find_element(By.ID, 'txtDate')
date_picker_2.send_keys("31/05/2025")





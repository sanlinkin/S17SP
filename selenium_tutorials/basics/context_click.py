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
driver.get('https://demo.guru99.com/test/simple_context_menu.html')

'''4. Context Click/ Right click'''
right_click_me_btn = driver.find_element(By.XPATH, '//*[@id="authentication"]/span')
actions.context_click(right_click_me_btn).perform()




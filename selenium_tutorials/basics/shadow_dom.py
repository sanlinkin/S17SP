'''
Created on 2 Jun 2025

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

'''3. Enter text in Shadow Dom'''
'''3a. Locate shadow host'''
shadow_host = driver.find_element(By.ID, 'shadow_host')
                              
'''3b. Get shadow present in the shadow host'''                                
my_shadow_root = shadow_host.shadow_root 

'''3c Find the element inside shadow root'''
shadow_input_text_field = my_shadow_root.find_element(By.CSS_SELECTOR, 'input[type=text]:nth-child(5)')
shadow_input_text_field.send_keys("Neymar")











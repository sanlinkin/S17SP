'''
Created on 24 May 2025

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
driver.get('https://demo.automationtesting.in/Frames.html')

'''3. Clicking on iframe within in an iframe'''
iframe_btn = driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a')
iframe_btn.click()
#('---------OR--------')
# iframe_with_in_an_iframe = driver.find_element(By.PARTIAL_LINK_TEXT, 'iframe with in an iframe')
# iframe_with_in_an_iframe.click()





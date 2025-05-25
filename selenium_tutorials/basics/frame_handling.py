'''
Created on 24 May 2025

@author: Sandeep
'''
from selenium import webdriver
from selenium.webdriver.common.by import By


'''1.Launching the Chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://demo.automationtesting.in/Frames.html')

'''3. Switch to iframe'''
driver.switch_to.frame('singleframe')

'''4. Enter text in Frame'''
input_text_bx = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
input_text_bx.send_keys("Messi")





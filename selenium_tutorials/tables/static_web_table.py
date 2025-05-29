'''
Created on 29 May 2025

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

'''3. Creating an Object from ActionChains class'''
actions = ActionChains(driver)

'''4. Scrolling'''
actions.scroll_by_amount(0, 1800).perform()

'''3. Print value from each cell'''
cell_21 =driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]')
cell_21_text = cell_21.text
print(cell_21_text)

cell_22 =driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]')
cell_22_text = cell_22.text
print(cell_22_text)

cell_23 =driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]')
cell_23_text = cell_23.text
print(cell_23_text)

cell_24 =driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]')
cell_24_text = cell_24.text
print(cell_24_text)

# //*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]
# //*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]
# //*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]
#
# //*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]
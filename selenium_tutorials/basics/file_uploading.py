'''
Created on 19 May 2025

@author: Sandeep
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

'''1.Launching the Chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Upload single file'''
single_file_input = driver.find_element(By.ID, 'singleFileInput')
single_file_input.send_keys('C:\\Users\Dell\Desktop\\Neymar.xlsx')
single_upload_btn = driver.find_element(By.XPATH, '//*[@id=\"singleFileForm\"]/button')
single_upload_btn.click() 

# '''4. Upload multiple file'''
# multiple_file_input = driver.find_element(By.ID, 'multipleFileInput')
# multiple_file_input.send_keys('C:\\Users\Dell\Desktop\\Neymar.xlsx')
# multiple_file_input.send_keys('C:\\Users\Dell\Desktop\\Messi.xlsx')
#
# multiple_upload_btn = driver.find_element(By.XPATH, '')
# multiple_upload_btn.click() 




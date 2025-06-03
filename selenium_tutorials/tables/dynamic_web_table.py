'''
Created on 31 May 2025

@author: Sandeep
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.action_chains import ActionChains

'''1.Launching the Chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Dynamic Table'''
row_list = driver.find_elements(By.XPATH, '//*[@id="rows"]/tr')
rows_count = len(row_list)

expected_name = input("Name: ")

for j in range(2, rows_count+1):
    name_cell = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{j}]/td[1]')
    actual_name = name_cell.text
    if expected_name == actual_name:
        memory_cell = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{j}]/td[contains(text(),"MB")and not(contains(text(), "/s"))]')
        memory = memory_cell.text
        print(memory)
        break
else:
    print("Memory not found")


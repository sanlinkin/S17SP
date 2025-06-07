'''
Created on 31 May 2025

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

'''3. Print value from each cell---> (2nd row, 1st element---> 21)'''

row_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
row_count = len(row_list)

column_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td')
column_count = len(column_list)

expected_book = input("Enter book name: ")

'''4. print the books price'''

name = input("Enter book price: ")

for j in range(2, row_count+1):
    book_name = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[1]')
    actual_book_name = book_name.text
    
    if actual_book_name == name:
        price = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[4]')
        price = price.text
        print("Price of ", book_name, "is", price)
        break
else:
    print("book not found")





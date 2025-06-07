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

'''3. Print value from each cell---> (2nd row, 1st element---> 21)'''

row_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
row_count = len(row_list)
expected_book = input("Enter Book Name: ")

column_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td')
column_count = len(column_list)
name = input("enter book price: " )

for j in range(2, row_count+1):
    for i in range(1, column_count+1):
        book_name = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[1]')
        book_name  = book_name.text
        print(book_name)
        book_price = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[4]')
        book_price = book_price.text
    if book_name == name:
        print("price of", book_name, "is", book_price)
        break
else:
    print("Book Not Found")
















'''

#3. Print value from each cell---> (2nd row, 1st element---> 21)'''
# cell_21 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]')
# cell_21_value = cell_21.text
# print(cell_21_value)
#
# cell_22 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]')
# cell_22_value = cell_22.text
# print(cell_22_value)
#
# cell_23 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]')
# cell_23_value = cell_23.text
# print(cell_23_value)
#
# cell_24 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]')
# cell_24_value = cell_24.text
# print(cell_24_value)
#
#
# cell_31 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]')
# cell_31_value = cell_31.text
# print(cell_31_value)














# cell_21_22_23_24 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]/td[2]/td[3]/td[4]')
# cell_21_22_23_24_text = cell_21_22_23_24.text
# print(cell_21_22_23_24_text)


# //*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]
# //*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]
# //*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]
#
# //*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]




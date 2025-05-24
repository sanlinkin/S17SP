'''
Created on 15 May 2025

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

'''3. Enter name'''
name_txt_bx = driver.find_element(By.ID, 'name')
name_txt_bx.send_keys("Sandeep")
#name_txt_bx.click()

'''4. Enter email'''
email_txt_bx = driver.find_element(By.ID, 'email')
email_txt_bx.send_keys("sanlinkin9925@gmail.com")

'''5. Enter phone'''
phone_txt_bx = driver.find_element(By.ID, 'phone')
phone_txt_bx.send_keys("9901309238")

'''6. Enter address'''
address_input = driver.find_element(By.ID, 'textarea')
address_input.send_keys("3rd stage, Vijayanagar, Mysore")


'''7. Enter Gender'''
gender_radiobutton = driver.find_element(By.ID, 'male')
gender_radiobutton.click()
# gender_radiobutton = driver.find_element(By.ID, 'female')
# gender_radiobutton.click()

'''8. Enter Days'''
days_radiobutton = driver.find_element(By.ID, 'saturday')
days_radiobutton.click()

'''9. Enter Country'''
country_txt_bx = driver.find_element(By.ID, 'country')
country_txt_bx.click()
country_txt_bx = driver.find_element(By.CSS_SELECTOR, '#country> option:nth-child(9)')
country_txt_bx.click()

# '''10. Enter Colors'''
# colors_txt_bx = driver.find_element(By.ID, 'colors')
# colors_txt_bx.click()
# colors_txt_bx = driver.find_element(By.CSS_SELECTOR, '#colors> option:nth-child(blue)')
# colors_txt_bx.click()

'''11. Date Picker_1 '''
datepicker1_input = driver.find_element(By.ID, 'datepicker')
datepicker1_input.send_keys('05/20/2025')
datepicker1_btn = driver.find_element(By.XPATH, '//*[@id="datepicker"]')
datepicker1_btn.click() 


'''11. Date Picker_2 '''
datepicker2_input = driver.find_element(By.ID, 'txtDate')
datepicker2_input.send_keys('05/31/2025')
datepicker2_btn = driver.find_element(By.XPATH, '//*[@id="txtDate"]')
datepicker1_btn.click()





























































































































































































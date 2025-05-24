'''
Created on 11 May 2025

@author: Sandeep

'''
'''
# ("----- for Chrome Browser -----")
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://selenium.dev/')

#("-----OR------")

from selenium.webdriver import Chrome

driver = Chrome()
driver.get('https://selenium.dev/')
'''
'''
# ("----- for Edge Browser -----")

from selenium.webdriver import Edge

driver = Edge()
driver.get('https://selenium.dev/')
'''


from selenium import webdriver

'''1.Launching the Chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Validate the navigation is successfull'''
current_page_title=driver.title
print(current_page_title)

expected_page_title="Automation Testing Practice"

if current_page_title == expected_page_title:
    print("Test is Passed!!")
else:
    print("Test Failed!!")


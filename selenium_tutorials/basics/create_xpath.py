'''
Created on 29 May 2025

@author: Sanndeep
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
driver.get('https://testautomationpractice.blogspot.com/')


'''3. wiki search'''

wiki_search_input = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
wiki_search_input.send_keys("Selenium disulfide")

wiki_search_btn = driver.find_element(By.XPATH, '//*[@id="wikipedia-search-result-link"]/a')
wiki_search_btn.click() 












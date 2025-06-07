'''
Created on 7 Jun 2025

@author: Dell
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class OrangeHRMLoginTest(unittest.TestCase):


    def test_navigation_to_login_page(self):
        '''1. Launching the Chrome browser'''
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options)
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)
        driver.implicitly_wait(10)
        
        '''2. Navigating to OrangeHRM login page'''
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        
        '''3. Enter name'''
        enter_user_name = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        enter_user_name.send_keys("Admin")
        
        '''4. Enter password'''
        enter_user_password = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        enter_user_password.send_keys("admin123")
        
        '''5. Click on Login'''
        click_on_login = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button' )
        click_on_login.click()
        
        '''6. Validate whether navigation is successful'''
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/logi"
        expected_url_portion = "auth/login"
        actual_url = driver.current_url
        
        #self.assertEqual(actucal_url, expected_url, "Navigation to OrangeHRM login page is failed") #self.assertEqual(first, second, msg)
        self.assertIn(expected_url_portion, actual_url, "Navigation to OrangeHRM login page is failed") #self.assertIn(member, container, msg)
    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
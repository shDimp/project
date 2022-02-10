import time
import unittest
from selenium import webdriver
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))
from selenium.webdriver.chrome.service import Service

from Samplepro.SampleTest.pages.loginPage import LoginPage
from Samplepro.SampleTest.pages.homePage import HomePage

class Login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Service("C:\\Users\\mesus\\PycharmProjects\\selenium\\driver\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_page(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        # driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        # driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        # driver.find_element(By.ID,"btnLogin").click()
        # driver.find_element(By.ID,"welcome").click()
        # driver.find_element(By.LINK_TEXT,"Logout").click()
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.driver.close()
        #print(cls.driver.title)

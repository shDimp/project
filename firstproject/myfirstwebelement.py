from selenium import webdriver
from selenium.webdriver.firefox.service import Service
service =Service("../driver/geckodriver.exe")
driver=webdriver.Firefox(service=service)
driver.get("https://opensource-demo.orangehrmlive.com/")
var = driver.find_element("name", "txtUsername")
var.send_keys("Admin")
driver.find_element("name","txtPassword").send_keys("admin123")
driver.find_element("id","btnLogin").click()
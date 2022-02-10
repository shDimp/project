from selenium import webdriver
driver = webdriver.Chrome("../driver/chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("automation")
driver.find_element_by_name("btnk").click()
driver.close()
driver.quit()
print(driver)


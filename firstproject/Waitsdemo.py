from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ser = Service("../driver/chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com")
driver.find_element(By.NAME,"q").send_keys("testing")
wait = WebDriverWait(driver,10)
try:
    element = wait.until(EC.element_to_be_clickable((By.NAME,"btnK1")))
    print("element is clickable")
except:
    element.click()
    exit(1)

# driver.find_element(By.NAME,"btnK").click()
print("test Completed")
driver.close()
driver.quit()
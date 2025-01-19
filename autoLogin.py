from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://5.152.64.228:8280/fina-app/ui/index.html#fi")
driver.implicitly_wait(0.5)
driver.find_element(by=By.ID, value="login").send_keys("ilapachi")
driver.find_element(by=By.ID, value="password").send_keys("test1234")
driver.find_element(by=By.ID, value="languageSelect").click()
driver.find_element(By.XPATH,'//*[@value="ka_GE"]').click()
driver.find_element(by=By.ID, value="signInButton").click()
time.sleep(10)
driver.close()
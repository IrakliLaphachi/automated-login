from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

login = driver.find_element(by=By.ID, value="login")
password = driver.find_element(by=By.ID, value="password")
lang = driver.find_element(by=By.ID, value="languageSelect")
ka = driver.find_element(By.XPATH,'//*[@value="ka_GE"]')
signIn = driver.find_element(by=By.ID, value="signInButton")

driver.maximize_window()
driver.get("http://5.152.64.228:8280/fina-app/ui/index.html#fi")
driver.implicitly_wait(0.5)
login.send_keys("ilapachi")
password.send_keys("test1234")
lang.click()
ka.click()
signIn.click()
time.sleep(10)
driver.close()
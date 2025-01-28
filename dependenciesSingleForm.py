from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://ilapachi:test1234@5.152.64.228:8580/fina-app/ui/index.html")
driver.implicitly_wait(1)

sidebar = driver.find_element(by=By.ID, value="gela")
ActionChains(driver).move_to_element(sidebar).perform()

returns = driver.find_element(By.CSS_SELECTOR, 'div.MuiButtonBase-root:nth-child(15)')
ActionChains(driver).move_to_element(returns).perform()
ActionChains(driver).click(returns).perform()

main = driver.find_element(by=By.ID, value="/returndefinitions")
ActionChains(driver).move_to_element(main).perform()

driver.find_element(By.CSS_SELECTOR, ".css-1ww8w0e > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > div:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > span:nth-child(1) > input:nth-child(1)").click()

dependenciesBtn = driver.find_element(By.CSS_SELECTOR, 'div.css-lvyu5j:nth-child(4) > span:nth-child(1) > button:nth-child(1)')
dependenciesBtn.click()

time.sleep(10)
driver.close()
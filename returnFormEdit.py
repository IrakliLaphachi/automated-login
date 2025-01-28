import time
import random

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://ilapachi:test1234@5.152.64.228:8580/fina-app/ui/index.html")
driver.implicitly_wait(1)

sidebar = driver.find_element(by=By.ID, value="gela")
ActionChains(driver).move_to_element(sidebar).perform()

periods = driver.find_element(By.CSS_SELECTOR, 'div.MuiButtonBase-root:nth-child(15)')
ActionChains(driver).move_to_element(periods).perform()
ActionChains(driver).click(periods).perform()

main = driver.find_element(by=By.ID, value="/returndefinitions")
ActionChains(driver).move_to_element(main).perform()

returnForm = driver.find_element(By.CSS_SELECTOR, "div.css-1ix01nk:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > div:nth-child(1) > tr:nth-child(1)")
ActionChains(driver).move_to_element(returnForm).perform()

editButton = driver.find_element(By.CSS_SELECTOR, 'div.css-1ix01nk:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > div:nth-child(1) > tr:nth-child(1) > div:nth-child(7) > button:nth-child(1)')
ActionChains(driver).move_to_element(editButton).perform()
ActionChains(driver).click(editButton).perform()

returnTypes = driver.find_element(By.CSS_SELECTOR, '.css-f7ljxb > input:nth-child(2)')
ActionChains(driver).move_to_element(returnTypes).perform()
ActionChains(driver).click(returnTypes).perform()

r = random.randint(1, 19)
typeSelect = driver.find_element(By.CSS_SELECTOR, 'li.MuiButtonBase-root:nth-child(%r)'% int(r))
ActionChains(driver).move_to_element(typeSelect).perform()
ActionChains(driver).click(typeSelect).perform()

saveBtn = driver.find_element(By.CSS_SELECTOR, '.css-16lrbi9')
ActionChains(driver).move_to_element(saveBtn).perform()
ActionChains(driver).click(saveBtn).perform()
time.sleep(5)

driver.refresh()

time.sleep(10)
driver.close()
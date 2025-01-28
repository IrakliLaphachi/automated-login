from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://ilapachi:test1234@5.152.64.228:8580/fina-app/ui/index.html")
time.sleep(1)

sidebar = driver.find_element(by=By.ID, value="gela")
ActionChains(driver).move_to_element(sidebar).perform()

schedule = driver.find_element(By.CSS_SELECTOR, 'div.MuiButtonBase-root:nth-child(19)')
ActionChains(driver).move_to_element(schedule).perform()
ActionChains(driver).click(schedule).perform()
time.sleep(1)

main = driver.find_element(by=By.ID, value="/schedules")
ActionChains(driver).move_to_element(main).perform()

scheduleCode = driver.find_element(By.CSS_SELECTOR, '.css-1vv8zkg > table:nth-child(1) > tbody:nth-child(2) > div:nth-child(1) > tr:nth-child(1) > td:nth-child(2)')
ActionChains(driver).move_to_element(scheduleCode).perform()
time.sleep(1)

copyButton = driver.find_element(By.CSS_SELECTOR, '.css-1vv8zkg > table:nth-child(1) > tbody:nth-child(2) > div:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)')
ActionChains(driver).move_to_element(copyButton).perform()
ActionChains(driver).click(copyButton).perform()

time.sleep(10)
driver.close()
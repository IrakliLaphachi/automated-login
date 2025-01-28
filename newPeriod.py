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

periods = driver.find_element(By.CSS_SELECTOR, 'div.MuiButtonBase-root:nth-child(16)')
ActionChains(driver).move_to_element(periods).perform()
ActionChains(driver).click(periods).perform()

main = driver.find_element(by=By.ID, value="/perioddefinitions")
ActionChains(driver).move_to_element(main).perform()

addNew = driver.find_element(By.CSS_SELECTOR, "div.css-38jp5q:nth-child(2) > button:nth-child(1)")
ActionChains(driver).move_to_element(addNew).perform()
ActionChains(driver).click(addNew).perform()

window = driver.find_element(By.CSS_SELECTOR, 'div.MuiPaper-root:nth-child(3)')
ActionChains(driver).move_to_element(window).perform()

periodTypes = driver.find_element(By.CSS_SELECTOR, '.css-16jn7jx > div:nth-child(2) > input:nth-child(2)')
ActionChains(driver).move_to_element(periodTypes).perform()
ActionChains(driver).click(periodTypes).perform()

typeSelect = driver.find_element(By.CSS_SELECTOR, 'li.MuiButtonBase-root:nth-child(2)')
ActionChains(driver).move_to_element(typeSelect).perform()
ActionChains(driver).click(typeSelect).perform()

startPeriod = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div/div/input')
startPeriod.clear()
startPeriod.send_keys('01/01/2025')

time.sleep(10)
driver.close()
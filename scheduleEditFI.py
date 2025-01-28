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

scheduleItem = driver.find_element(By.CSS_SELECTOR, '.css-1vv8zkg > table:nth-child(1) > tbody:nth-child(2) > div:nth-child(1) > tr:nth-child(1)')
ActionChains(driver).move_to_element(scheduleItem).perform()
time.sleep(1)

edit = driver.find_element(By.CSS_SELECTOR, '.css-1vv8zkg > table:nth-child(1) > tbody:nth-child(2) > div:nth-child(1) > tr:nth-child(1) > div:nth-child(15) > button:nth-child(1)')
ActionChains(driver).move_to_element(edit).perform()
ActionChains(driver).click(edit).perform()

editWindow = driver.find_element(By.CSS_SELECTOR, 'div.MuiPaper-root:nth-child(3)')
ActionChains(driver).move_to_element(editWindow).perform()

fiEdit = driver.find_element(By.CSS_SELECTOR, '.css-jjbgoo > div:nth-child(2) > input:nth-child(2)')
ActionChains(driver).move_to_element(fiEdit).perform()
ActionChains(driver).click(fiEdit).perform()

fiFolder = driver.find_element(By.CSS_SELECTOR, 'div.ReactVirtualized__Table__row:nth-child(1)')
ActionChains(driver).move_to_element(fiFolder).perform()
ActionChains(driver).double_click(fiFolder).perform()

fiCheckbox = driver.find_element(By.CSS_SELECTOR, 'div.ReactVirtualized__Table__row:nth-child(2) > div:nth-child(3) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
ActionChains(driver).move_to_element(fiCheckbox).perform()
ActionChains(driver).click(fiCheckbox).perform()

ActionChains(driver).move_to_element(fiEdit).perform()
ActionChains(driver).click(fiEdit).perform()

driver.find_element(By.CSS_SELECTOR, '.css-1qhkgy4 > button:nth-child(2)').click()
time.sleep(1)

checkPass = driver.find_element(by=By.ID, value='notistack-snackbar').text

if checkPass == "GENERAL_ERROR":
    print("fail")
else:
    print("pass")

time.sleep(10)
driver.close()
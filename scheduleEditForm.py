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

formEdit = driver.find_element(By.CSS_SELECTOR, '.css-10y2wf3 > div:nth-child(2) > input:nth-child(2)')
ActionChains(driver).move_to_element(formEdit).perform()
ActionChains(driver).click(formEdit).perform()

formEditCheckbox = driver.find_element(By.CSS_SELECTOR, '.Mui-checked > input:nth-child(1)')
ActionChains(driver).move_to_element(formEditCheckbox).perform()
ActionChains(driver).click(formEditCheckbox).perform()

ActionChains(driver).move_to_element(formEdit).perform()
ActionChains(driver).click(formEdit).perform()

driver.find_element(By.CSS_SELECTOR, '.css-1qhkgy4 > button:nth-child(2)').click()
time.sleep(1)

checkPass = driver.find_element(by=By.ID, value='notistack-snackbar').text

if checkPass == "GENERAL_ERROR":
    print("fail")
else:
    print("pass")

time.sleep(10)
driver.close()
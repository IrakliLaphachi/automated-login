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

catalog = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div[2]/div/div[8]')
ActionChains(driver).move_to_element(catalog).perform()
ActionChains(driver).click(catalog).perform()

main = driver.find_element(by=By.ID, value="mainCatalog")
ActionChains(driver).move_to_element(main).perform()

row = driver.find_element(By.CSS_SELECTOR, 'tr.MuiTableRow-root:nth-child(1)')
ActionChains(driver).move_to_element(row).perform()
time.sleep(1)

deleteBtn = driver.find_element(By.CSS_SELECTOR, 'tr.MuiTableRow-root:nth-child(1) > div:nth-child(13) > button:nth-child(2)')
ActionChains(driver).move_to_element(deleteBtn).perform()
ActionChains(driver).click(deleteBtn).perform()

confirm = driver.find_element(By.CSS_SELECTOR, '.css-12slxt5')
ActionChains(driver).move_to_element(confirm).perform()
ActionChains(driver).click(confirm).perform()
time.sleep(1)

checkPass = driver.find_element(by=By.ID, value='notistack-snackbar').text

if checkPass == "deleted":
    print("pass")
else:
    print("fail")

time.sleep(10)
driver.close()
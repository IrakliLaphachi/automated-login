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

addNew = driver.find_element(By.CSS_SELECTOR, "button.MuiButton-text:nth-child(3)")
ActionChains(driver).move_to_element(addNew).perform()
ActionChains(driver).click(addNew).perform()

window = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]')
ActionChains(driver).move_to_element(window).perform()

newCode = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/input')
newCode.send_keys("555")

nextBtn = driver.find_element(By.CSS_SELECTOR, '.css-174ufm4 > button:nth-child(1)')
nextBtn.click()
nextBtn.click()

structName = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[2]/div[3]/div/div[2]/ul/div/li/div[1]/div/input')
structName.send_keys("1")

saveBtn = driver.find_element(By.CSS_SELECTOR, '.css-1rcn0vx')
saveBtn.click()
time.sleep(1)

checkPass = driver.find_element(by=By.ID, value='notistack-snackbar').text

if checkPass == "catalogCreateSuccess":
    print("pass")
else:
    print("fail")

time.sleep(10)
driver.close()
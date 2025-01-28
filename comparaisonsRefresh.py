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

comparisons = driver.find_element(By.CSS_SELECTOR, 'div.MuiButtonBase-root:nth-child(12)')
ActionChains(driver).move_to_element(comparisons).perform()
ActionChains(driver).click(comparisons).perform()

main = driver.find_element(by=By.ID, value="/comparisons")
ActionChains(driver).move_to_element(main).perform()

driver.find_element(By.CSS_SELECTOR, ".css-npbq9x > button:nth-child(2)").click()

time.sleep(10)
driver.close()
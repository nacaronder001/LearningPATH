from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
parent_window = driver.current_window_handle


driver.find_element(By.CLASS_NAME, "blinkingText").click()


windows = driver.window_handles
driver.switch_to.window(windows[1])
x = driver.find_element(By.XPATH, "//div/p[2]/strong/a").text

x = driver.find_element(By.PARTIAL_LINK_TEXT, "mentor@rahulshettyacademy.com").text

for i in windows:
    if i != parent_window:
        driver.switch_to.window(parent_window)



driver.find_element(By.CSS_SELECTOR, "#username").send_keys(x)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("12345678")
driver.find_element(By.CLASS_NAME, "form-control").click()
driver.find_element(By.XPATH, "//div/select/option[3]").click()
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://rahulshettyacademy.com/client")

email = "demo1234@gmail.com"
password = 123456789


driver.find_element(By.XPATH, "//a[text()='Forgot password?']").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys(password)
driver.find_element(By.XPATH, "//form/div[3]/input").send_keys(password)
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div[class='overlay-container']")))
alert = driver.find_element(By.CSS_SELECTOR, "div[class='overlay-container']").text
message = "Password Changed Successfully"
assert (message == alert)

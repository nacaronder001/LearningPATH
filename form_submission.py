
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select



PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://rahulshettyacademy.com/angularpractice/")


#fullname #email #password
driver.find_element(By.NAME, "name").send_keys("Demo1234")
driver.find_element(By.NAME, "email").send_keys("Demo1234@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")


# Static Dropdown (Choices)
choice = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
choice.select_by_index(1)




driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
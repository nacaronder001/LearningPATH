
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.implicitly_wait(5)
fruit_name = "Apple"
file_path = "C:/Users/nacar/Downloads/download.xlsx"


driver.find_element(By.ID, "downloadButton").click()


file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)

locator = (By.CSS_SELECTOR, "div[class='Toastify__toast-body']")
wait = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locator)))
message = driver.find_element(*locator).text
print(message)


column = driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id")
apple = driver.find_element(By.XPATH, "//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+column+"-undefined']").text
print(apple)



driver.close()
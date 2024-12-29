from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

#SELECTING THE SECOND OPTION
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "radio2":
        checkbox.click()
        assert checkbox.is_selected()
        break
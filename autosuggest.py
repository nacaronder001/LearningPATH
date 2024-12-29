from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://rahulshettyacademy.com/dropdownsPractise")
driver.implicitly_wait(5)



driver.find_element(By.ID, "autosuggest").send_keys("Tu")
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "Turkey":
        country.click()
        break

try:
    country = driver.find_element(By.ID, "autosuggest").get_attribute("value")
    assert country == "Turkey"
except AssertionError as i:
    print("Invalid Country")

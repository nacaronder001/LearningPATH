from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
driver.maximize_window()

#CLICKING ON SHOP
driver.find_element(By.XPATH, "//a[.='Shop']").click()

#SECOND PAGE
phone_list = driver.find_elements(By.XPATH, "//div/h4 / a")

#PICKING THE BLACKBERRY PHONE
for phone in phone_list:
    if phone.text == "Blackberry":
        driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[4]").click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

#ADDING THE COUNTRY TURKEY
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Tur")
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Turkey")))
driver.find_element(By.LINK_TEXT, "Turkey").click()


driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success!" in message
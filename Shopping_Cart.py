from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)

#TYPING BER ON THE SEARCH BAR
driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)

# LIST of Products
actual_list = []
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for result in products:
    actual_list.append(result.find_element(By.XPATH, "h4").text)
print(actual_list)


#ADDING THE PRODUCTS IN THE CART
products = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
for product in products:
    product.click()

#PROCEED TO CHECKOUT
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//div[.='PROCEED TO CHECKOUT']").click()

#USING PROMOTION
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
time.sleep(5)


print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)


# TOTAL PRICES IN CART
prices = driver.find_elements(By.XPATH, "//td[5] / p")
sum = 0
for price in prices:
    sum += int(price.text)


total_amount = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text) #total = 388
assert total_amount == sum


#MAKING SURE TOTAL PRICE WITH DISCOUNT IS LESS THAN THE ACTUAL AMOUNT WITHOUT DISCOUNT
discount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text) #discount = 349.2
assert discount < total_amount



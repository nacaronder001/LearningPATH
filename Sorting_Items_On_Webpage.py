from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
SortedWebList = driver.find_elements(By.XPATH, "//tr/td[1]")

web_sorted_list = []
my_sorted_list = []
for by_name in SortedWebList:
    web_sorted_list.append(by_name.text)


my_sorted_list = web_sorted_list
my_sorted_list.sort()

assert my_sorted_list == web_sorted_list
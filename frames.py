from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()


#using id
driver.switch_to.frame("singleframe")

text = driver.find_element(By.TAG_NAME, "input")
text.send_keys("My demo, Onder")

#return to home default
driver.switch_to.default_content()


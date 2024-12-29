from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")


driver.find_element(By.LINK_TEXT, "Click Here").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.find_element(By.TAG_NAME, "h3").text)  #New Window
driver.close()
driver.switch_to.window(windows[0])
print(driver.find_element(By.TAG_NAME, "h3").text) # Opening a new window
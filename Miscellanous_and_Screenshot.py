from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")


PATH = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=PATH, options=chrome_options)
driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);") #it scrolls all the way down to bottom
driver.get_screenshot_as_file("screen.png") #takes a screenshot
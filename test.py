from selenium import webdriver
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox()
driver.get("http://google.com/")
driver.quit()

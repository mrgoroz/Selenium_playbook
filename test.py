from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://google.com/")
driver.quit()

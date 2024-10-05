from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()

# Open a web page
driver.get('https://example.com')

# Find an element and interact with it
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python automation')
search_box.submit()

# Close the browser
driver.quit()

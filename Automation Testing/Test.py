from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

# Initialize ChromeDriver
driver = webdriver.Chrome()

# Navigate to the OrangeHRM login page
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(1)

# Find and enter the Username
driver.find_element(By.NAME, 'username').send_keys('Admin')
time.sleep(1)

# Find and enter the Password
driver.find_element(By.NAME, 'password').send_keys('admin123')
time.sleep(1)

# Click the Login button
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

# Extract information from the page before making changes
text = driver.find_element(By.CLASS_NAME, 'oxd-userdropdown-name').text
print("Username (Before): " + text)
time.sleep(1)

# Go to the My Info page
driver.find_element(By.LINK_TEXT, 'My Info').click()
time.sleep(1)

# Generate a random word to replace the Lastname
word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()
word = random.choice(WORDS)

# Replace the Lastname field with the generated word
lastName = driver.find_element(By.NAME, 'lastName')
lastName.click()
time.sleep(1)
lastName.send_keys(Keys.COMMAND + "a")
lastName.send_keys(Keys.DELETE)
time.sleep(1)
lastName.send_keys(word)
time.sleep(1)

# Click the Save Button
driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
time.sleep(2)

# Refresh the page
driver.refresh()
time.sleep(2)

# Extract information from the page after making changes
text = driver.find_element(By.CLASS_NAME, 'oxd-userdropdown-name').text
print("Username (After): " + text)
time.sleep(1)

# Close the browser
driver.quit()
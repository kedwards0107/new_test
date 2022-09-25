from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

PATH = "/Users/mack/Desktop/Programming/Python/Selinium_2022/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")
print(driver.title)

link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    button.click()

    # Can move to previous page with:
    #driver.back()
    # Can move forward page with:
    #driver.forward()
    # Can clear entry in input field with:
    #"name of found element".clear() ex. element.clear()


except:
    driver.quit()
# driver.quit()



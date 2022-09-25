from wsgiref.simple_server import sys_version
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import getpass

PATH = "/Users/mack/Desktop/Programming/Python/Selinium_2022/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.costco.com/")
print(driver.title)

link = driver.find_element(By.ID, "header_sign_in")
link.click()

try:
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "myaccount-react-t")
    #     ))
    # link = driver.find_element(By.ID, "myaccount-react-t")
    # link.click()
    print("1st check")
    login = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "signInName")
        ))
    print("2nd check")
    email = driver.find_element(By.ID, "signInName")
    #email_entry.click()
    my_pass = getpass.getpass()
    email.send_keys(my_pass)
    password = driver.find_element(By.ID, "password")
    my_pass = getpass.getpass()
    password.send_keys(my_pass)
    enter = driver.find_element(By.ID, "next")
    enter.click()
    #email_entry.send_keys(Keys.RETURN)
#myaccount-react-t
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     element.click()

#     button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "sow-button-19310003"))
#     )
#     button.click()

#     # Can move to previous page with:
#     #driver.back()
#     # Can move forward page with:
#     #driver.forward()
#     # Can clear entry in input field with:
#     #"name of found element".clear() ex. element.clear()

test = "new"

except:
    driver.quit()
#driver.quit()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

url = "https://www.brainyquote.com/"

PATH = "/Users/mack/Desktop/Programming/Python/Selinium_2022/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get(url)
print(driver.title)

search = driver.find_element(By.ID, 'hmSearch')
search.send_keys("love")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "quotesList"))
    )
    
except:
    driver.quit()

# main = driver.find_element(By.ID, "quotesList")
# print(main.text)
articles = element.find_elements(By.TAG_NAME, "a")

for article in articles:
    # quote = element.find_element(By.TAG_NAME, "a")
    print(article.text)

driver.quit()
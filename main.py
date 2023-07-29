import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

website = "https://www.adamchoi.co.uk/teamgoals/detailed"

os.environ["PATH"] += r";D:\Platzi\python\webscrapper"
driver = webdriver.Chrome()
driver.get(website)

wait = WebDriverWait(driver, 10)

all_matches_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//label[@analytics-event="All matches"]'))
)
all_matches_button.click()

countrySelection = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//select[@id="country"]'))
)
select = Select(countrySelection)
select.select_by_visible_text("USA")

matches = driver.find_elements(By.TAG_NAME, "td")

for match in matches:
    print(match.text)

time.sleep(30)

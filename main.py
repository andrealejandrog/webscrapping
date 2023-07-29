import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

import pandas as pd

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

time.sleep(15)

matches = driver.find_elements(By.TAG_NAME, "tr")

dates = []
home_team = []
score = []
away_team = []
home = []

for match in matches:
    home = match.find_element(By.XPATH, "./td[1]").text
    dates.append(home)
    home_team.append(match.find_element(By.XPATH, "./td[2]").text)
    score.append(match.find_element(By.XPATH, "./td[3]").text)
    away_team.append(match.find_element(By.XPATH, "./td[4]").text)


data = pd.DataFrame()
data["Dates"] = dates
data["Home Team"] = home_team
data["Score"] = score
data["Away Team"] = away_team

data.to_excel("Data.xlsx")


time.sleep(30)

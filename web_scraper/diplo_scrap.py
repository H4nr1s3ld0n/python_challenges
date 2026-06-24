from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests
import os
import time
from pathlib import Path

# Creates the folder if needed and opens Selenium 

output_dir = Path('monde-diplomatique')
output_dir.mkdir(exist_ok=True)
driver = webdriver.Firefox()
driver.get('https://www.monde-diplomatique.fr/')

# Search for the first article on the website, retreives description and url

wait = WebDriverWait(driver, 5)
une = driver.find_element(By.XPATH, "//a[.//div[@class='unarticle yalogo blogs']]")
description = une.text
url = une.get_attribute('href')

print(f"Downloading : {description}")
print(f"URL : {url}")

# Downloads the main article and handles HTTP errors

try:
	response = requests.get(f'{url}', timeout=10)
	response.raise_for_status()

	filename = f"{os.path.basename(url)}.html"
	filepath = output_dir / filename

	with open(filepath, 'wb') as f:
		for chunk in response.iter_content(chunk_size=100000):
			f.write(chunk)

	print(f"Saved in : {filepath}")

except requests.exceptions.HTTPError as e:     
	print("HTTP error occurred:", e) 
except requests.exceptions.RequestException as e:     
	print("A request error occurred:", e)

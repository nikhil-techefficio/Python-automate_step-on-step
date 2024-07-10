from datetime import datetime
import glob
import shutil
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, TimeoutException
import time
import os
import re
current_directory = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_directory, 'chromedriver.exe')
current_directory = os.path.dirname(os.path.abspath(__file__))
download_directory = os.path.join(current_directory, 'downloads')

options = ChromeOptions()
#options.add_argument("--headless")  # Run in headless mode
options.add_experimental_option('prefs', {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
service = ChromeService(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Firefox(service=service, options=firefox_options)
driver.get('https://vahan.parivahan.gov.in/vahan4dashboard/vahan/vahan/view/reportview.xhtml')
# Refresh the page and stay on it
driver.refresh()

# Optionally, you can add a wait to ensure the page has fully reloaded
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    print("Page refreshed and ready.")
except TimeoutException:
    print("Page took too long to refresh.")

# Keep the browser open to stay on the page (especially important in headless mode)
time.sleep(10)  # Adjust the sleep duration as needed

# Close the driver when done
driver.quit()
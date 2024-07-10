from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import os

# Set up the Chrome WebDriver
current_directory = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_directory, 'chromedriver.exe')

options = ChromeOptions()
#options.add_argument("--headless")  # Remove this line if you want to see the browser
service = ChromeService(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

# Open YouTube
driver.get('https://www.youtube.com')

# Search for something
search_query = 'Hindi trending song' # Search prompt
search_box = wait.until(EC.presence_of_element_located((By.NAME, 'search_query')))
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Wait for the results to load and click on the first result
wait.until(EC.presence_of_element_located((By.ID, 'video-title')))
first_result = driver.find_element(By.ID, 'video-title')
first_result.click()

# Wait for the video to load
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'html5-video-player')))

# Pause the video
time.sleep(10)  # Give it some time to start playing
video_player = driver.find_element(By.CLASS_NAME, 'html5-video-player')
video_player.send_keys(Keys.SPACE)  # Space bar toggles play/pause

# Play the video
time.sleep(2)
video_player.send_keys(Keys.SPACE)  # Space bar toggles play/pause

# Speed up the video
time.sleep(2)
driver.execute_script("document.getElementsByTagName('video')[0].playbackRate = 2.0")  # Set playback speed to 2x

# Increase volume (YouTube shortcuts don't allow for volume change directly; simulate key presses)
for _ in range(5):
    video_player.send_keys(Keys.ARROW_UP)  # Arrow Up key increases volume
    time.sleep(0.5)  # Adjust delay as needed

# Go back to YouTube home
driver.get('https://www.youtube.com')

# Close the driver
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)

# Youtube Example
""" driver.get("https://www.youtube.com/results?search_query=tiny+train+models")

results = driver.find_elements(By.ID, 'video-title')

for videoTitle in results:
    print(videoTitle.text)
"""

# Spotify global daily charts example
driver.get("https://kworb.net/spotify/country/global_daily.html")

results = driver.find_elements(By.CSS_SELECTOR, ".text.mp")

songTitles = []

""" for songTitle in results:
    songTitles.append(songTitle.text)
"""
for i in range(20):
    songTitles.append(results[i].text)

results = driver.find_elements(By.XPATH, "//*[@id='spotifydaily']/tbody/tr")

songStreams = []

""" for list in results:
    songStreams.append(list.find_element(By.CSS_SELECTOR, ":nth-child(7)").text)
"""
for i in range(20):
    songStreams.append(results[i].find_element(By.CSS_SELECTOR, ":nth-child(7)").text)

plt.bar(songTitles, songStreams)
plt.xlabel('Song Titles')
plt.ylabel('Total Streams')

plt.show()
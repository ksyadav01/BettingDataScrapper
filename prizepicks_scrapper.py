import pandas as pd
import requests
import json
from pandas import json_normalize
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://api.prizepicks.com/projections')

authors = driver.find_element(By.CSS_SELECTOR, 'pre')
#print(authors.text)

json_object = json.loads(authors.text)

lines = json_object['data']
players = json_object['included']


LeaguePlayers = []
Leagues = {}

# Gets all sports categories for bets
# Creates corrosponding sublists in cumulative Leagues dictionary
for player in players:
    if player["type"] == "league":
        Leagues[player['attributes']['name']] = [player['id']]
        #print(player)
# Gets individual player data and stores, also creates empty lines structure
for player in players:
    if player["type"]!= "new_player":
        continue

    player_league = player['attributes']['league']
    updated_player = {"id": player['id'], "image_url": player['attributes']['image_url'], "name": player['attributes']['name'],
                      "position": player['attributes']['position'], "team": player['attributes']['team'], "lines": []}
    Leagues[player_league].append(updated_player)

# Gets the lines and predictions for corrosponding player, stores it in lines sublist
#for line in lines:
for line in lines:
    sport = line['relationships']['league']['data']['id']
    current_league = Leagues
    # current_league contains the league and all players for the specified sport of this line
    for league in Leagues:
        if league[0] == sport:
            current_league = league
            # cycles through all entries
            for entry in league:

            break
    for 


with open('players.json', 'w', encoding='utf-8') as f:
    json.dump(Leagues, f, ensure_ascii=False, indent=4)

with open('lines.json', 'w', encoding='utf-8') as f:
    json.dump(lines, f, ensure_ascii=False, indent=4)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random as rng
BASE_LINK = "https://2048game.com/"
service = Service(executable_path= "chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(BASE_LINK)
input_element = driver.find_element(By.TAG_NAME, "html")
tiles = driver.find_element(By.CLASS_NAME, "tile-container")
moves = [Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT]
isOver = False
max = 0 
count = 0
while(isOver==False):
      move = rng.choice(moves)
      input_element.send_keys(move)
      try:
        driver.find_element(By.CLASS_NAME, "game-over")
        isOver = True
        tiles = tiles.find_elements(By.CLASS_NAME, "tile")
        for tile in tiles:
            broj = int(tile.find_element(By.CLASS_NAME, "tile-inner").text)
            print(f"{broj}\t")
            if(max < broj):
                  max = broj
      except:
           count =+1 

print("-----------KRAJ--------------")
print(f"IGRA JE TRAJALA {count} POTEZA I MAKSIMALAN BROJ JE {max}")
time.sleep(5)
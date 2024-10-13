from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




class MusicBot(webdriver.Chrome):
    def __init__(self, driver_path ="chromedriver.exe" ):
       service = Service(executable_path=driver_path)
       self.service = service
       super(MusicBot, self).__init__() 
       self.maximize_window()
    
    def land_first_page(self, base_link = "https://www.youtube.com/"):
        self.get(base_link)
    
    def search_song(self, song = "Timeleass-Weeknd"):
        WebDriverWait(self, 5).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        search_box = self.find_element(By.NAME, "search_query")
        search_box.send_keys(song)
        search_box.send_keys(Keys.ENTER)
    
    def find_first_video(self, song = "Timeless-Weeknd"):
        song_name = song.split('-')[0]
        song_author = song.split('-')[1]
        print(f"{song_name}    {song_author}")
        WebDriverWait(self, 5).until(
            EC.presence_of_element_located((By.ID, "video-title"))
        )
        videos = self.find_elements(By.ID, "video-title")
        print(f'{len(videos)}\n')
        count = 0
        found = False
        while(found == False):
            if song_name.lower() in videos[count].text.lower() and song_author.lower() in videos[count].text.lower():
                print(count)
                found = True
            else: count += 1

        videos[count].click()
    
    def download_video(self):
        current_link = self.current_url
        self.get("https://ytmp3s.nu/hvwg/")
        input_element = self.find_element(By.ID, "url")
        input_element.clear()
        input_element.send_keys(current_link)
        submit_button =  self.find_element(By.XPATH, "//input[@value='Convert']")
        submit_button.click()
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Download')]"))
        )
        download_button = self.find_element(By.XPATH, "//a[contains(text(),'Download')]")
        download_button.click() 
        time.sleep(1)
        tabs = self.window_handles
        self.switch_to.window(tabs[1])
        self.close()
        self.switch_to.window(tabs[0])
       
       
        

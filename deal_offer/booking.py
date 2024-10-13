from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class BookingBot(webdriver.Chrome):
    def __init__(self, driver_path ="chromedriver.exe" ):
       service = Service(executable_path=driver_path)
       self.service = service
       super(BookingBot, self).__init__() 
       self.maximize_window()
    
    def land_first_page(self, base_link = "https://www.booking.com/"):
        self.get(base_link)
        time.sleep(3)

    
    def close_pop_up(self):
        try:
            time.sleep(2)
            close_button = self.find_element(By.XPATH, "//button[@aria-label = 'Dismiss sign-in info.']")
            close_button.click()
        except:
            pass
    
    def send_props(self, city='Amsterdam', adults=8, check_in= "2024-10-10", check_out = "2024-10-19"):
        city_input = self.find_element(By.ID, ":rh:")
        city_input.send_keys(city)
        time.sleep(1)
        first_option = self.find_element(By.ID, "autocomplete-result-0")
        first_option.click()
        time.sleep(1)
        check_in_date_button = self.find_element(By.XPATH, f"//span[@data-date = '{check_in}']").click()
        check_out_date_button = self.find_element(By.XPATH, f"//span[@data-date = '{check_out}']").click()
        self.find_element(By.XPATH, "//button[@data-testid = 'occupancy-config']").click()
        adults_count = int(self.find_element(By.CLASS_NAME, "d723d73d5f").text)
        if adults_count == adults:
            pass
        elif adults_count > adults:
            while(adults_count > adults):
                self.find_element(By.CLASS_NAME, "e91c91fa93").click()
                adults_count = int(self.find_element(By.CLASS_NAME, "d723d73d5f").text)
        else:
            while(adults_count < adults):
                self.find_element(By.CLASS_NAME, "f4d78af12a").click()
                adults_count = int(self.find_element(By.CLASS_NAME, "d723d73d5f").text)
        self.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)

    def apply_filter(self, stars=3):
        time.sleep(2)
        filter_groups = self.find_element(By.XPATH, "//div[@data-filters-group='class']")
        print("nasao sam filter ")
        print(filter_groups.text)
       
        elements = filter_groups.find_element(By.XPATH, f"//div[ @data-filters-item='class:class={stars}']")
        elements.click()
        time.sleep(5)
        min_slider = self.find_element(By.CSS_SELECTOR, 'input[aria-label="Min."]')
        max_slider = self.find_element(By.CSS_SELECTOR, 'input[aria-label="Max."]')
        time.sleep(2)
        list = self.find_element(By.XPATH, "//button[@data-testid = 'sorters-dropdown-trigger']")
        list.click()
        # XPath to find the button using its data-id and aria-label
        button = self.find_element(By.XPATH, '//button[@data-id="bayesian_review_score" and @aria-label="Top reviewed"]')
        button.click()
        # time.sleep(1000)
        # tags = list.find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, 'li')
        # print(len(tags))
        # tags[7].click()
        time.sleep(5)
    
    def find_top_reviewed(self):
        properties  = self.find_elements(By.XPATH, "//div[@data-testid='property-card']")
        first_property = properties[0]
        first_property.find_element(By.TAG_NAME, "a").click()
        time.sleep(5)

    def get_picture(self):
        windows = self.window_handles
        self.switch_to.window(windows[1])
        body = self.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        self.save_screenshot("screen.png")
        time.sleep(50)

       
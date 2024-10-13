from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
webdriver = webdriver.Chrome(service=service)
webdriver.get("https://www.accuweather.com")
featured_location = webdriver.find_element(By.CLASS_NAME, "featured-location") 
webdriver.maximize_window()
featured_location.click()
WebDriverWait(webdriver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//a[span[text()='Daily']]"))
)
daily_forecast = webdriver.find_element(By.XPATH, "//a[span[text()='Daily']]")
daily_forecast.click()
temp_element = webdriver.find_element(By.CLASS_NAME, "temp")
high = temp_element.find_element(By.CLASS_NAME, "high").text
low = temp_element.find_element(By.CLASS_NAME, "low").text.strip("/")
phrase = webdriver.find_element(By.CLASS_NAME, "phrase").text
sentence = f"Here is weather forecast for today\nMax tempereature: {high}\nMinimum temperature: {low}\n{phrase}"
print(sentence)
webdriver.get("https://x.com/")

WebDriverWait(webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/login')]"))
)
log_in_button = webdriver.find_element(By.XPATH, "//a[contains(@href, '/login')]")
log_in_button.click()
username = 'prognozas2s'
lozinka = 'jakojakalozinka'
WebDriverWait(webdriver, 5).until(
    EC.presence_of_element_located(( By.XPATH, "//input[@name='text' and @type='text']"))
)
username_input = webdriver.find_element( By.XPATH, "//input[@name='text' and @type='text']")
username_input.send_keys(username)
next = webdriver.find_element(By.XPATH, "//button//span[text()='Next']")
next.click()
WebDriverWait(webdriver, 10).until(
    EC.presence_of_element_located(( By.XPATH, "//input[@name='password' and @type='password']"))
)
password_input = webdriver.find_element( By.XPATH, "//input[@name='password' and @type='password']")
password_input.send_keys(lozinka)
log = webdriver.find_element(By.XPATH, "//button//span[text()='Log in']")
log.click()
WebDriverWait(webdriver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/compose/post')]"))
)
compose = webdriver.find_element(By.XPATH, "//a[contains(@href, '/compose/post')]")
compose.click()
#close_pop_up = webdriver.find_element(By.XPATH, "//button[@]")
time.sleep(5)
text_element = webdriver.find_element(By.XPATH, "//div[@aria-label = 'Post text']")
text_element.send_keys(sentence)
post_button = webdriver.find_element(By.XPATH, "//button[@data-testid='tweetButton']")
post_button.click()
time.sleep(100)

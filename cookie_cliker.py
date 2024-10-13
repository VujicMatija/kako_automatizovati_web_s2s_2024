from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


BASE_LINK = "https://orteil.dashnet.org/cookieclicker/"
service = Service(executable_path="chromedriver.exe")
webdriver = webdriver.Chrome(service=service)
webdriver.get(BASE_LINK)
webdriver.maximize_window()
WebDriverWait(webdriver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'English')]"))
)
langugage_button = webdriver.find_element(By.XPATH, "//div[contains(text(), 'English')]")
langugage_button.click()
cookie_id = "bigCookie"
WebDriverWait(webdriver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)
cookie_button = webdriver.find_element(By.ID, cookie_id)
prefix = "product"
while(1):
    cookies = int(webdriver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",",""))
    for x in  range(0, 19):
        productPrice = webdriver.find_element(By.ID, (prefix + "Price" + str(x))).text.replace(",","")
        if not productPrice.isdigit():
            continue
        productPrice = int(productPrice)
        if(cookies >= productPrice):
            productId = prefix + str(x) 
            productElement = webdriver.find_element(By.ID, productId)
            productElement.click()
    cookie_button.click()

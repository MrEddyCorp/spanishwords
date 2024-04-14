from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import data as dt
import time



url = "https://lapalabradeldia.com/"
_words = dt.getWordsBySize(5)
words = []


for word in _words:
    word =  word.replace("á","a")
    word =  word.replace("é","e")
    word =  word.replace("í","i")
    word =  word.replace("ó","o")
    word =  word.replace("ú","u")
    words.append(word)

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)

time.sleep(5)
button = driver.find_elements(By.TAG_NAME,"button")
button[33].click()
board = driver.find_element(By.ID,'board-all')
board.send_keys("edgar")
board.send_keys(Keys.ENTER)
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from env import ACCOUNT, PASSWORD


URL = 'https://www.imdb.com/'
IMDB_LOGIN_BTN = '//*[@id="imdbHeader"]/div[2]/div[5]/a'
IMDB_LOGIN_BY_GOOGLE_BTN = '//*[@id="signin-options"]/div/div[1]/a[4]'
GOOGLE_LOGIN_ACCOUNT_INPUT = '//*[@id="identifierId"]'
GOOGLE_LOGIN_NEXT_BTN = '//*[@id="identifierNext"]/div/button'


# Open the Imdb
driver = webdriver.Chrome()
driver.get(URL)

# Enter Login
login_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, IMDB_LOGIN_BTN)))
login_btn.click()

login_google_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, IMDB_LOGIN_BY_GOOGLE_BTN)))
login_google_btn.click()

input_gmail_address = WebDriverWait(driver, 5).until(lambda d: d.find_element(By.XPATH, GOOGLE_LOGIN_ACCOUNT_INPUT))
input_gmail_address.clear()
input_gmail_address.send_keys(Keys.ENTER, ACCOUNT)

continue_google_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, GOOGLE_LOGIN_NEXT_BTN)))
continue_google_btn.click()


print(ACCOUNT, PASSWORD)


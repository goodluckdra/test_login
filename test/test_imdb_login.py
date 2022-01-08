from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://www.imdb.com/'
IMDB_LOGIN = '/html/body/div[2]/nav/div[2]/div[5]/a'
IMDB_LOGIN_BY_GOOGLE = '/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div/div[1]/a[4]'

# Open the Imdb
driver = webdriver.Chrome()
driver.get(URL)

# Enter Login
login_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, IMDB_LOGIN)))
login_btn.click()

login_google_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, IMDB_LOGIN_BY_GOOGLE)))
login_google_btn.click()









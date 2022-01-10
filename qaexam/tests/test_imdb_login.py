from selenium.common import exceptions
from selenium.webdriver.chrome import options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import seleniumwire.undetected_chromedriver.v2 as uc
from unittest.mock import patch
from utils import file_utils
import time

from env import ACCOUNT, PASSWORD, PROFILE_PATH, USER_NAME
import imdb_login


URL = 'https://www.imdb.com/'
IMDB_LOGIN_BTN = '//*[@id="imdbHeader"]/div[2]/div[5]/a'
IMDB_LOGIN_BY_GOOGLE_BTN = '//*[@id="signin-options"]/div/div[1]/a[4]'
GOOGLE_LOGIN_ACCOUNT_INPUT = '//*[@id="identifierId"]'
GOOGLE_LOGIN_ACCOUNT_BTN = '//*[@id="identifierNext"]/div/button'
GOOGLE_LOGIN_PW_INPUT = '//*[@id="password"]/div[1]/div/div[1]/input'
GOOGLE_LOGIN_PW_BTN = '//*[@id="passwordNext"]/div/button'
USER_NAME_XPATH = '//*[@id="imdbHeader"]/div[2]/div[5]/div/label[2]/div/span'

def test_name_equals_main():
        with patch.object(imdb_login, "__name__", "__main__"):
                
                # initiate the driver
                options = uc.ChromeOptions()
                options.add_argument("--ignore-certificate-error")
                options.add_argument("--ignore-ssl-errors")
                options.add_argument( f"--user-data-dir={PROFILE_PATH}")
                options.add_argument('--disable-sync')
                driver = uc.Chrome(options=options)
                driver.get(URL)

                # # to choose log in via google account
                # login_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, IMDB_LOGIN_BTN)))
                # login_btn.click()
                # login_google_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, IMDB_LOGIN_BY_GOOGLE_BTN)))
                # login_google_btn.click()

                # # enter email and password to log in
                # input_gmail_address = WebDriverWait(driver, 5).until(lambda d: d.find_element(By.XPATH, GOOGLE_LOGIN_ACCOUNT_INPUT))
                # input_gmail_address.send_keys(Keys.ENTER, ACCOUNT)
                # continue_google_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, GOOGLE_LOGIN_ACCOUNT_BTN)))
                # continue_google_btn.click()
                # input_gmail_pw = WebDriverWait(driver, 5).until(lambda d: d.find_element(By.XPATH, GOOGLE_LOGIN_PW_INPUT))
                # time.sleep(3)
                # input_gmail_pw.send_keys(Keys.ENTER, PASSWORD)
                # continue_google_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, GOOGLE_LOGIN_PW_BTN)))
                # continue_google_btn.click()


                # to get the account name
                try:
                        user_name = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH, USER_NAME_XPATH).text)
                        if user_name != USER_NAME:
                                driver.save_screenshot(file_utils.screenshot_path_name(login=False))
                        else:
                                driver.save_screenshot(file_utils.screenshot_path_name(login=True))
                except TimeoutException as e:
                        driver.save_screenshot(file_utils.screenshot_path_name(login=False))

                assert user_name == USER_NAME


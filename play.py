# coding=UTF-8
import os, argparse

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import utils
import platform

MABINOGI_URL = "https://event.beanfun.com/mabinogi/E20210715/Index.aspx"

def main(cd_time):
    driver_path = get_chrome_driver()

    for user in users:
        driver = get_driver(driver_path)
        start_new_session(driver)
        login(driver, user)

        for category_idx in range(0, 6):
            vote(driver, category_idx)
        stop_session(driver)
        time.sleep(cd_time)

def vote(driver, category_idx):
    driver.execute_script("arguments[0].click();", get_vote_category(driver, category_idx))
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "artwork-box__img"))
    )

    for i in range(0, 3):
        candidate_btns = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"a[class=\"artwork-box\"][area=\"{category_idx + 1}\"]"))
        )

        driver.execute_script("arguments[0].click();", candidate_btns[i])

        vote_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "artworkPop-aside-btn__vote"))
        )
        vote_btn.click()

        click_vote_exit_btn(driver)
        time.sleep(1)


def click_vote_exit_btn(driver):
    for j in range(10):
        try:
            vote_exit_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'gbox-close'))
            )
            vote_exit_btn.click()
            return
        except StaleElementReferenceException:
            time.sleep(0.5)


def get_vote_category(driver, idx):
    artwork_tab_lists = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "artwork-tab-list"))
    )

    return artwork_tab_lists.find_elements(By.TAG_NAME, "a")[idx]

def get_chrome_driver():
	driver_path = os.path.dirname(os.path.abspath(__file__)) + '/driver/'
	if platform.system() == 'Windows':
		return driver_path + "win32/chromedriver.exe"
	elif platform.system() == 'Darwin':
		return driver_path + "mac64/chromedriver"
	else:
		raise Exception('Not supported os')
		
def start_new_session(driver):
    driver.get(MABINOGI_URL)

def stop_session(driver):
    driver.close()

def get_driver(driver_path):
    driver = webdriver.Chrome(driver_path)
    return driver

def login(driver, user):
    driver.execute_script("return $('a[class=\"event-btn__vote\"]')[0]").click()
    driver.execute_script("return $('a[class=\"gbox-btn btn\"]')[0]").click()
    login_routine(driver, user)
    time.sleep(3)

def login_routine(driver, user):
    # Login elements is in iframe, should switch to it
    login_iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ifmForm1"))
    )
    driver.switch_to_frame(login_iframe)
    login_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "btn_login"))
    )
    account = driver.find_element_by_id("t_AccountID")
    account.send_keys(user["account"])
    password = driver.find_element_by_id("t_Password")
    password.send_keys(user["password"])
    login_btn.click()

    # Choose game account
    game_account_selector = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ddl_service_account"))
    )
    for option in game_account_selector.find_elements_by_tag_name('option'):
        if option.text == user["game_account"]:
            option.click()
            driver.find_element_by_id("btn_send_service_account").click()
            break

def log_out(driver):
    log_out_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "i13"))
    )
    log_out_btn.click()


def filter_ignore_accounts(users, ignore_accts):
    return [x for x in users if x['account'] not in ignore_accts]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mabinogi 2021 summer vote')
    parser.add_argument('--cd', dest='cd_time', default=0, help='Cd time between accounts (sec.)')
    parser.add_argument('--ignore', dest='ignore_accounts', help='Ignore these accounts in account.json, split by comma')

    args = parser.parse_args()

    users = utils.load_json("account.json")
    if args.ignore_accounts is not None:
        users = filter_ignore_accounts(users, [x.strip() for x in args.ignore_accounts.split(',')])

    print('%s Mabinogi accounts' % (len(users)))
    print('Will wait %s seconds between accounts...' % args.cd_time)

    main(args.cd_time)
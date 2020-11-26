from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
import getpass
import os
import sys
import time

PATH = f"{os.environ['HOME']}/Web_Crawler/.chromedriver"
# driver = webdriver.Chrome(PATH)
def clear():
    os.system('clear')


def sa_bank():
    return input('Fill in a bank: ').lower()


def login_banking(bank):
    if 's' in bank:
        username = input("Welcome to login\n\nEnter Username: ")
        password = getpass.getpass(prompt='Enter password: ')
        clear()
        driver = webdriver.Chrome(PATH)
        site = driver.get('https://onlinebanking.standardbank.co.za/#/login')
        time.sleep(2)
        username_bar = driver.find_element_by_xpath('//*[@id="username"]')
        # ActionChains(driver).move_to_element(username_bar).click(username_bar).perform()
        username_bar.send_keys(username, Keys.ENTER)
        username_bar.send_keys(Keys.ENTER)
        print('Please wait...')
        time.sleep(3)
        print('performing transactions')
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/ng-include[1]/div/div/div[2]/div[7]/ibr-button/comp-lib-sb-button/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(password, Keys.ENTER)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/ibr-strong-auth-password/div/div/div[2]/form/div/ibr-button-group/div/div/ibr-button[1]/comp-lib-sb-button/button').click()
        otp_confirm = input('Did you get OTP y/n: ').lower()
        if otp_confirm == 'y':
            otp = getpass.getpass(prompt='OTP: ')
            driver.find_element_by_id('otp').send_keys(otp, Keys.ENTER)
            driver.find_element_by_xpath('//*[@id="submit-otp-button"]/button').click()
            driver.find_element_by_id('otp').send_keys(Keys.ENTER)
            input("what to do")
        else:
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="-button"]/button').click()
            print('OTP RESENT...')
clear()
bank = sa_bank()
clear()
login_banking(bank)

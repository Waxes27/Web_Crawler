from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import sys

# import time



def clear():
    os.system('clear')


def globals_():
    global i,driver,filter_
    driver = ''
    i = ['q']
    clear()
    print("Sort searches: \n\n - h - For highest to lowest\n - l - For lowest to highest")
    filter_ = input(' > ').lower()


def init():
    global driver
    global gsm_driver
    global specs
    PATH = f"{os.environ['HOME']}/Web_Crawler/.chromedriver"

    while len(i[-1]) > 0:
        print('######################')
        i.append(input('What item(s) are we looking for: '))
    
    specs = input("Specs on GSMARENA? (ENTER for no): ")
    driver = webdriver.Chrome(PATH)
    # if len(specs) > 0:
    #     gsm_driver = webdriver.Chrome(PATH)
        # gsm_arena()

    driver.get('https://www.olx.co.za')


def gsm_arena():
    gsm = gsm_driver.get('https://www.gsmarena.com/')
    gsm_search = gsm_driver.find_element_by_id('topsearch-text')
    gsm_search.send_keys(i[1], Keys.ENTER)


def sort_olx(filter_):
    if filter_ == 'l':
        sort_by_lowest = driver.find_element_by_xpath('//*[@id="container"]/main/div/section/div/div/div[4]/div[2]/div/div[1]/div/div[2]/ul/li[3]/div')
        sort_by_lowest.click()
    elif filter_ == 'h':
        sort_by_highest = driver.find_element_by_xpath('//*[@id="container"]/main/div/section/div/div/div[4]/div[2]/div/div[1]/div/div[2]/ul/li[4]/div')
        sort_by_highest.click()
    else:
        pass


def main():
    init()
    driver.implicitly_wait(6)
    search_bar = driver.find_element_by_xpath('//*[@id="container"]/header/div/div/div[2]/div/div/div[2]/div/form/fieldset/div/input')
    search_btn = driver.find_element_by_xpath('//*[@id="container"]/header/div/div/div[2]/div/div/div[3]')
    search_bar.send_keys(i[1], Keys.ENTER)

    sort_by = driver.find_element_by_xpath('//*[@id="container"]/main/div/section/div/div/div[4]/div[2]/div/div[1]/div/div[2]/div')
    if len(filter_) != 0:
        sort_by.click()
    sort_olx(filter_)
    # if len(specs) > 0:
    #     gsm_arena()


if sys.argv[-1].lower() == 'h' or sys.argv[-1].lower() == 'l':
    filter_ = sys.argv[-1].lower()
    driver = ''
    i = ['q']
    clear()
    main()
    clear()
else:
    driver = ''
    i = ['q']
    clear()
    print("Sort searches: \n\n - h - For highest to lowest\n - l - For lowest to highest")
    filter_ = input(' > ').lower()
    clear()
    main()
    clear()

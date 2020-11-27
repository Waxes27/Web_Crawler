from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import sys
import time

songs = {
    '1' : ['. A Tale of 2 Citiez - J-cole','https://www.youtube.com/watch?v=PB7gyS1TsYo&list=OLAK5uy_mvsSsaJ7aXJKopbPykpDdG9h0xotLliJE&index=5'],
    '2' : ['. New Light - Justice Der','https://www.youtube.com/watch?v=gl3fQ3MiJS8'],
    '3' : ['. Yonkers - Tyler the Creator','https://www.youtube.com/watch?v=XSbZidsgMfw'],
    '4' : ['. Nymano - beauty','https://www.youtube.com/watch?v=PRZs9LXLy6s'],
    '5' : ['. Juan Rios - Cascada','https://www.youtube.com/watch?v=5ccgR3fyf2g'],
    '6' : ['. Kevin Momo - Lately (feat. Blissful Sax)','https://www.youtube.com/watch?v=sutroWBOis0']
}
# print(songs['1. A Tale of 2 Citiez - J-cole'])
os.system('clear')
print("Pick your song of the day...\n\n")
for k,v in songs.items():
    print(f"{k}{v[0]}")

song_name = input('\nPick a number: \n')
# print()
PATH = f"{os.environ['HOME']}/Web_Crawler/.chromedriver"

# print(songs[song_name][1])
driver = webdriver.Chrome(PATH)

# driver.get('https://www.olx.co.za')
driver.get(songs[song_name][1])
play = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[5]/button')
# /html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[5]/button

time.sleep(2)
play.click()
driver.minimize_window()
# search_bar = driver.find_element_by_id('search')

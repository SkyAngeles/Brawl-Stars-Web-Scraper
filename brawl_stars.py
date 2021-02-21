import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

os.system('cls')

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get('https://brawltime.ninja/tier-list/map')

for _ in range(2):
    os.system('cls')
    print('\ncollecting data\n')
    time.sleep(.5)
    os.system('cls')
    print('\ncollecting data.\n')
    time.sleep(.5)
    os.system('cls')
    print('\ncollecting data..\n')
    time.sleep(.5)
    os.system('cls')
    print('\ncollecting data...\n')
    time.sleep(.5)
    os.system('cls')
    print('\ncollecting data....\n')
    time.sleep(.5)
    os.system('cls')
os.system('cls')

html = driver.page_source
driver.close()

soup = BeautifulSoup(html, 'html.parser')
livegames = soup.findAll('div', class_='flex flex-wrap justify-center items-end')

for games in livegames:

    gamemodes = []
    games.findAll('div', class_='mr-auto')
    for title in games:
        gamemode = title.find('h1', class_='text-xl').text
        map = title.find('h2', class_='whitespace-nowrap text-xl').text
        gamemodes.append(f"| {gamemode.strip().upper()} | {map.strip().upper()} |")

    allwinrates = []
    allbrawlers = []
    games.findAll('div', class_='bg-cover bg-center bg-filter relative z-10 px-3 py-2')
    for game in games:
        winrates = game.findAll('a', class_='flex-1 flex flex-col justify-end items-center mx-px')
        rates = [x.text.replace('Win', '').strip() for x in winrates]
        allwinrates.append([rates[0], rates[1], rates[2], rates[3], rates[4]])

        brawlers = [x for x in winrates]
        game_brawlers = []
        for brawler in brawlers:
            brawler.find('a', href=True, text=True)
            game_brawlers.append(str(brawler['href']).replace('/tier-list/brawler/', '').replace('_', ' ').title())
        allbrawlers.append(game_brawlers)

    for mode in range(len(gamemodes)):
        print(gamemodes[mode])
        for a in range(len(allbrawlers[mode])):
            print(f"{allbrawlers[mode][a]}\t{allwinrates[mode][a]}".expandtabs(15))
        print('\n')


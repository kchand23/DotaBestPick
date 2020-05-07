import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.dotabuff.com"
heroes = []
hero_matchups = {}
 
def get_heroes():
    page = requests.get(BASE_URL + "/heroes",headers={'user-agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('div', class_ = "hero-grid")

    heroes = results[0].find_all('a', href = True)

    heroes_parsed = []

    for i in heroes:
        heroes_parsed.append(i['href'].split("/")[-1])

    return heroes_parsed

def get_matchup(hero):
    page = requests.get(BASE_URL + "/heroes/" + hero + "/counters" ,headers={'user-agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('table', class_= "sortable")

    hero_grid = results[0].find_all('tbody')

    rows = hero_grid[0].find_all('tr')

    for matchup in rows:

        matchup_row = matchup.find_all('a')

        matchup_name = matchup_row[0]['href'].split("/")[-1]

        print(str(matchup_name) + " " + matchup.find_all('td')[2].text)


heroes = get_heroes()


get_matchup(heroes[0])

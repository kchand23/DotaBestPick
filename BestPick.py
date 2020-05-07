import requests

BASE_URL = "https://www.dotabuff.com"
 
def get_heroes():
    page = requests.get(BASE_URL + "/heroes",headers={'user-agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('div', class_ = "hero-grid")

    heroes = results[0].find_all('a', href = True)

    return heroes

from bs4 import BeautifulSoup

heroes = get_heroes

for i in heroes:
    print(i['href'])
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

    matchup_dict = {}

    for matchup in rows:

        matchup_row = matchup.find_all('a')

        matchup_name = matchup_row[0]['href'].split("/")[-1]

        matchup_dict[matchup_name] = matchup.find_all('td')[2].text

    return matchup_dict


heroes = get_heroes()

match = {}

for i in heroes:
    match[i] = 0


#get 5 heroes from user based on current match
for i in range(5):
    curr_hero = input("Enter hero" + str(i + 1) + ": ")
    matchup = get_matchup(curr_hero)
    for i in heroes: 
        if i != curr_hero:
            match[i] += float(matchup[i].split("%")[0])

#Sort the dictionary based on values
sorted = {k: v for k, v in sorted(match.items(), key=lambda item: item[1])}


print("Top 10 picks:  ")

top10 = sorted_list[:9]
for i in top10:
    print(i + ": " + str(sorted[i]))

#Get heroe names in order of advantage. 
sorted_list = list(sorted.keys())
print("The top 10 picks are: ")

#get last 10 and reverse to get the last 10 best heroes
last10 = sorted_list[-9:]
last10 = [ele for ele in reversed(last10)] 


for i in last10:
    print(i + ": " + str(sorted[i]))

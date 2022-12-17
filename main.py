import requests
all_heroes = '/all.json'
url = 'https://akabab.github.io/superhero-api/api'
list_heroes = requests.get(url + all_heroes).json()
hero = {'id': 0, 'name': 0, 'intelligence': 0}
for d in list_heroes:
    if d['name'] in ['Hulk', 'Captain America', 'Thanos']:
        powerstats = requests.get(url + f'/powerstats/{d["id"]}.json').json()
        if powerstats['intelligence'] > hero['intelligence']:
            hero.update(
                id=d['id'], name=d['name'],
                intelligence=powerstats['intelligence']
            )

if __name__ == '__main__':
    print(
        f'Самый умный герой {hero["name"]} c интелектом - '
        f'{hero["intelligence"]}'
    )

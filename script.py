import numpy as np
import pandas as pd
import sklearn
import requests
from bs4 import BeautifulSoup
import json
import re

#url = 'http://ad.betcity.ru/d/off/champs?ids_sp=3&rev=3&ver=390&csn=eepugw'
url = 'http://ad.betcity.ru/d/stats?a=cl&p=3&ver=167&csn=ooca9s'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

# запрос json со списком чемпионатов
r = requests.get(url, headers = headers) 
y = json.loads(r.text)

soap = BeautifulSoup(y['reply']['html'], features='html.parser')

items = soap.find_all('option', value=re.compile('^3:'))
list_of_leagues = []  # все лиги, получили
for item in items:
    list_of_leagues.append(str(item.get('value')))

print('1st stage done!')

list_of_all = []
for league in list_of_leagues:
    url = 'http://ad.betcity.ru/d/stats?a=tt&p=' + league.split(':')[0] + '%3A' + league.split(':')[1] + '&ver=167&csn=ooca9s'
    a = requests.get(url, headers = headers)
    new_soap = BeautifulSoup(json.loads(a.text)['reply']['html'], features='html.parser')
    matches_following = new_soap.find('div', {'id':'matchesFollowing'})
    if (film_list is not None)




with open('test.html', 'w', encoding='utf-8') as output_file:
    output_file.write(str(list_of_leagues))  # .encode('cp1251')
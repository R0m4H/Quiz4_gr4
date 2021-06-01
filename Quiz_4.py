import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

h = {'Accept-Language': 'en-US'}
ind = 0

file = open('anime.csv', 'w', encoding='UTF-8', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['Title', 'Rating', 'Information'])

while ind<500:
    url = 'https://myanimelist.net/topanime.php?limit=' + str(ind)
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    anime_list = soup.find('table', class_='top-ranking-table')
    all_anime = anime_list.find_all('tr', class_='ranking-list')
    for each in all_anime:
        title_info = each.find('div', class_='di-ib')
        title = title_info.h3.text
        information_block = each.find('div', class_='information')
        info = information_block.text
        info = info.replace('\n', '')
        rating_info = each.find('div', class_='js-top-ranking-score-col')
        rating = rating_info.span.text
        file_obj.writerow([title, rating, info])



    ind += 50
    sleep(randint(1,5))
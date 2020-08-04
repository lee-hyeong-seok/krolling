import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

naver_movie = soup.select('ul.lst_detail_t1 > li')

for i in naver_movie:
    code = i.select_one('dl>dt>a')['href']
    movie_code = code.split('code=')[1]
    title = i.select_one('dl>dt>a').get_text()

    movie_data = {
        'code' : movie_code,
        'title' : title
    }

    with open('movie_data.csv','a',encoding='utf8') as f:
        fieldnames = ['code','title'] 
        csvwriter = csv.DictWriter(f, fieldnames=fieldnames)
        csvwriter.writerow(movie_data) 




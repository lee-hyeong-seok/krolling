import requests
from bs4 import BeautifulSoup
import csv

soup_objects = []

for i in range(1,102,10):

    base_url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start='
    s_url = i
    e_url = '&refresh_start=0'

    URL = base_url+str(s_url)+e_url

    response = requests.get(URL)


    soup = BeautifulSoup(response.text,'html.parser')
    soup_objects.append(soup)

for soup in soup_objects:


    news_section = soup.select(
        'div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01] > li' 
    )

    for i in news_section:
        a_tag = i.select_one('dl>dt>a')

        news_title = a_tag['title']
        news_link = a_tag['href']

        news_data = {
            'title' : news_title,
            'hyperlink' : news_link

        }

        with open('./naver_news.csv','a',encoding='utf8') as csvfile:
            fieldnames = ['title','hyperlink']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writerow(news_data)
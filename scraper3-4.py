import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt"
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')
titles = soup.find_all(
    'span', {'class': 'lx-stream-post__header-text gs-u-align-middle'})
title_list = []
for title in titles:
    title_list.append(title.getText())

links = soup.find_all(
    'a', {'class': 'qa-heading-link lx-stream-post__header-link'})

tag_list = []
for lk in links:
    # print('https://www.bbc.com' + lk.get('href'))
    lk = 'https://www.bbc.com' + lk.get('href')
    sub_res = requests.get(lk)
    sub_soup = BeautifulSoup(sub_res.text, 'lxml')
    tags = sub_soup.find_all('li', {'class': 'bbc-1msyfg1 e1hq59l0'})
    for tag in tags:
        tag_list.append(tag.find('a').getText())
print(tag_list)
import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt"
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')
titles = soup.find_all(
    'span', {'class': 'lx-stream-post__header-text gs-u-align-middle'})
title_list = []
for title in titles:
    title_list.append(title.getText())

print(title_list)

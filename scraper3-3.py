import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt"
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')
print(soup)
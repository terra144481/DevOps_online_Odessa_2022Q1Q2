from urllib.request import urlopen
from bs4 import BeautifulSoup
 
html = urlopen('https://code.visualstudio.com/docs/python/python-tutorial')
bs = BeautifulSoup(html.read(), 'html.parser')
title = bs.find_all('title')
for t in title:
    print(t.get_text())
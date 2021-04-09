#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

starttime=time.time()

def priceTracker(url):
    page = urlopen(url)
    soup = bs4.BeautifulSoup(page,'html.parser')
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'lxml')
    #print(soup.prettify())
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

print('Real Time Stock Price (Updated every 15 seconds)')

while True:
    print('Current price of FB is ' + str(priceTracker('https://in.finance.yahoo.com/quote/FB?p=FB')))
    print('Current price of GOOGLE is ' + str(priceTracker('https://in.finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch')))
    time.sleep(15.0 - ((time.time() - starttime) % 15.0))


# In[ ]:





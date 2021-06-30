#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
from bs4 import BeautifulSoup

#洗網頁資料
url = requests.get("https://rate.bot.com.tw/xrt")
soup = BeautifulSoup(url.text)
text_d = soup.find_all('div',class_="hidden-phone print_show")
text_r = soup.find_all('td',class_="rate-content-sight text-right print_hide")
dollars = [e.text.replace('\n','').replace(' ','') for e in text_d]
Rates = [float(e.text.replace('\n','').replace(' ','').replace('-','0')) for e in text_r]
rates = [[Rates[x],Rates[x+1]] for x in range(0,len(Rates),2)]

#洗CSV資料
file = pd.read_csv("https://rate.bot.com.tw//xrt/flcsv/0/day")
data_buy = file['現金']
data_sell = file['現金.1']

#比對
for i in range(len(dollars)):
    if rates[i][0] != data_buy[i]:
        print(dollars[i],"即期買入:資料有誤!",rates[i][0],data_buy[i])
    if rates[i][1] != data_sell[i]:
        print(dollars[i],"即期賣出:資料有誤!",rates[i][1],data_sell[i])
print('完全符合!')


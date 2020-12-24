# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:33:19 2020

@author: Khizer-PC
"""

import requests 
from bs4 import BeautifulSoup
import csv
import pandas as pd


result = requests.get("https://www.whitehouse.gov/briefings-statements/")
print(result.status_code)
src = result.content

soup = BeautifulSoup(src,'lxml')

urls = []

for h2_tag in soup.find_all('h2'):
    a_tag = h2_tag.find('a')
    try:
        urls.append(a_tag.attrs['href'])
    except:
            pass 

lenght = len(urls)
print(lenght)
        
print(urls)

df = pd.DataFrame(urls)
df.to_csv('file.csv', index='false', header='false')         
            
    
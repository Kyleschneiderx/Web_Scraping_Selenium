#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:26:33 2019

@author: kyleschneider
"""

import urllib
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


dataset = pd.read_csv('healthline.com.csv')
q_list = dataset.iloc[0:3000,0]
kyleUse = q_list.tolist()


browser = webdriver.Chrome("/Users/kyleschneider/Desktop/Scraping/chromedriver")
# Tell Selenium to get the URL you're interested in.
browser.get("https://www.google.com/")

try_list = q_list

newList=[]
for search in try_list:
    inputElement = browser.find_element_by_name("q")
    inputElement.send_keys('%s'%search)
    inputElement.send_keys(Keys.ENTER)
    
    # Now that the page is fully scrolled, grab the source code.
    source_data = browser.page_source
    soup = BeautifulSoup(source_data,"html.parser")
    
    
    for link in soup.find_all('div', {'style' : 'padding-right:40px'}):
        print(link.text)
        newList.append(link.text)
        
    
    browser.get("https://www.google.com/")

browser.close()

re_list = list(dict.fromkeys(newList))

   
question_list = pd.DataFrame()
question_list['Questions']= newList   

question_list.drop_duplicates(subset ="Questions", 
                     keep = False, inplace = True) 

question_list.to_csv(r'question_list3.csv')

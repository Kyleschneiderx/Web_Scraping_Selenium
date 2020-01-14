#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 13:02:39 2019

@author: kyleschneider
"""


from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome("/Users/kyleschneider/Desktop/Scraping/chromedriver")
# Tell Selenium to get the URL you're interested in.
browser.get("https://www.quora.com/topic/Marketing")

source_data = browser.page_source
soup = BeautifulSoup(source_data,"html.parser")

questList=[]
for link in soup.find_all('span', {'class' : 'ui_qtext_rendered_qtext'}):
    print(link.text)
    questList.append(link.text)
    
    

browser = webdriver.Chrome("/Users/kyleschneider/Desktop/Scraping/chromedriver")
# Tell Selenium to get the URL you're interested in.
browser.get("https://www.google.com/")

try_list = questList


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


question_list = pd.DataFrame()
question_list['Questions']= newList 
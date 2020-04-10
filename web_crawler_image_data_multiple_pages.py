# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:44:50 2020

@author: foysal
"""
import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import os
import random

def page_control(max_pages):
    current_page = 1
    while(current_page<=max_pages):
        base_url = 'http://books.toscrape.com/'
        url = 'http://books.toscrape.com/catalogue/page-'+str(current_page)+'.html'
        #print(url)
        single_page_info(base_url,url)
        #page = requests.get(url)
        #soup = BeautifulSoup(page.content,'html.parser')
        #for url_list in soup.select('.next a'): #each page has only one next a
            #href = 'http://books.toscrape.com/'+url_list.get('href')
            #print(href)
            #single_page_info(href)
        current_page = current_page+1    

def single_page_info(base_url,url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    #print('base url:',base_url,' url :',url)
    # find images
    #find all img tag
    imgs = soup.find_all('img')
    #print(img)
    links = []
    for img in imgs:
        #get source attributes of the image
        link = img.get('src')
        #print('old link: ',link)
        #link = os.path.relpath(link, '../')
        link = link [3:] #remove first 3 character which are  ../
        #print('new link: ',link)
        if 'http://' not in link:
            #getting individual link
            link = base_url + link
        # store all image link in a list    
        links.append(link)
    print ('Image detected: ' +str(len(links)))
    print('Image link: ', str(links))  
    
    for i in range (len(links)):
        #filename = 'img{}.png'.format (i)
        filename = 'img{}.png'.format (random.randint(1,10000))
       # print(links[i])
        urllib.request.urlretrieve(links[i],filename)
        #print('done')
    
            
page_control(2)    
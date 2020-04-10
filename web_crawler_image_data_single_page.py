# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:05:36 2020

@author: foysal
"""
import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'http://books.toscrape.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
#print(soup)

# find images
#find all img tag
imgs = soup.find_all('img')
#print(img)
links = []
for img in imgs:
    #get source attributes of the image
    link = img.get('src')
    if 'http://' not in link:
        #getting individual link
        link = url + link
    # store all image link in a list    
    links.append(link)
#print('main url: ',url)    
print ('Image detected: ' +str(len(links)))
#print('Image link: ', str(links))  

for i in range (len(links)):
    filename = 'img{}.png'.format (i)
    urllib.request.urlretrieve(links[i],filename)
    #print(filename)
    #print(links[i])

# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:32:01 2021

@author: WALID CHEHTANE
"""

import requests
from bs4 import BeautifulSoup


#retrieving the website's html code
URL = 'https://www.cfcunderwriting.com'
page = requests.get(URL)
#creating a Beautiful Soup object
soup= BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())



#listing externally loaded resources
def External_re():
    #finding the images and resources with specific relation
    images=soup.find_all(['img'])
    rel=soup.find_all( attrs={ 'rel':['stylesheet','apple-touch-icon','icon','manifest','mask_icon','noindex']})
    #writing to a json file
    with open('resources.json', 'w') as json_file:
        json_file.write(str(images)+"\n")
        json_file.write(str(rel)+"\n")
    json_file.close()
    print('resources file created successfully')
    

#writing hyperlinks to a JSON file
def Get_links():
    links=soup.find_all(href=True)
    with open('hyperLinks.json', 'w') as json_file2:
        for i in links:
            json_file2.write(i.get('href', None)+"\n")
    json_file2.close()  
    print('hyperlinks file created successfully')




#if __name__=="__main__":
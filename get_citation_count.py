# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup
import datetime

files_to_update = ['index.html','myresearch.html','myteaching.html','publications.html']
page_url = "https://scholar.google.com.au/citations?hl=en&user=U5OApm0AAAAJ"

page = urllib2.urlopen(page_url)

soup = BeautifulSoup(page, 'html.parser')

cnt_box = soup.find('td', attrs={'class': 'gsc_rsb_std'})

cnt = cnt_box.text.strip()

current_date = datetime.datetime.now()
month_name = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
date_string = '{} {} {}'.format(month_name[current_date.month-1],current_date.day,current_date.year)

for file_name in files_to_update:
    with open(file_name, 'r') as file:
        data = file.readlines()
    
    for i,l in enumerate(data):
        if "Total Citations" in l:
            l = "<h3>Total Citation Count: {} </h3>\n".format(str(cnt))
        elif "Source: GoogleScholar" in l:
            l = "<h5>Source: GoogleScholar on {} </h5>\n".format(date_string)
        data[i] = l
    
    
    with open(file_name, 'w') as file:
        file.writelines( data )

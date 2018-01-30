# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup
import datetime

files_to_update = ['index.html','myresearch.html','myteaching.html','publications.html']
page_url = "https://scholar.google.com.au/citations?hl=en&user=U5OApm0AAAAJ"

page = urllib2.urlopen(page_url)

soup = BeautifulSoup(page, 'html.parser')

all_cnt_box = soup.find_all('td', attrs={'class': 'gsc_rsb_std'})[:]

cnt_box = all_cnt_box[0]
cnt_lo_box = all_cnt_box[1]

cnt = cnt_box.text.strip()
cnt_lo = cnt_lo_box.text.strip()

print(cnt)
print(cnt_lo)

current_date = datetime.datetime.now()
month_name = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
date_string = '{} {} {}'.format(month_name[current_date.month-1],current_date.day,current_date.year)


pub_citation_start='<p><h2>My research has <b>1975</b> citations, including <b>1901</b> the last 5 years</h2></p>'
src_start='<div class="w3-container"><h5>Source: GoogleScholar on Jan 18 2018</h5></div>'

rest_citation_start='<h3><b>Total Citation Count:'

for file_name in files_to_update:
    with open(file_name, 'r') as file:
        data = file.readlines()
    
    for i,l in enumerate(data):

        if rest_citation_start in l:
            l = '<h3><b>Total Citation Count: {} </b></h3>\n'.format(str(cnt))
        elif pub_citation_start in l:
            l = '<p><h2>My research has <b>{}</b> citations, including <b>{}</b> the last 5 years</h2></p>\n'.format(str(cnt),str(cnt_lo))
        elif src_start in l:
            l = '<div class="w3-container"><h5>Source: GoogleScholar on Jan 18 2018</h5></div>\n'.format(date_string)
        data[i] = l
    
    
    with open(file_name, 'w') as file:
        file.writelines( data )

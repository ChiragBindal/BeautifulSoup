#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:52:32 2023

@author: chiragbindal
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
android_url = "https://en.wikipedia.org/wiki/Android_version_history"
android_data = urlopen(android_url)
android_html = android_data.read()
android_data.close()

android_soup = soup(android_html , 'html.parser')
tables = android_soup.findAll('table' , {'class' : 'wikitable'})
android_table = tables[0];
headers = android_table.findAll('th')
column_titles = [ct.text[:-1] for ct in headers]
rows_data = android_table.findAll('tr' , {})[1:]
table_row = []
for row in rows_data :
  curr_row = []
  row_data = row.findAll('td' , {})
  for idx,data in enumerate(row_data) :
    curr_row.append(data.text[0:-1])
  table_row.append(curr_row)

filename = "android_version_history.csv"
with open(filename , 'w' , encoding='utf-8') as f :
  header_string = ','.join(column_titles)
  header_string += '\n'
  f.write(header_string)
  for row in table_row :
    row_strings = ""
    row_strings = ','.join(row)
    row_strings += '\n'
    f.write(row_strings)





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
print(android_table);

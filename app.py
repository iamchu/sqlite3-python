# How to use python and databases? 
# Which db suits more X purpose?
# How to automate db crud?
# Create a generic universally applicable template
# Which Data Structures are more conveniente to X purpose?

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os
import requests
import bs4

def main():
	grabCompanyCodes()

# grab BOVESPA company codes
def grabCompanyCodes():
	url = 'https://cotacoes.economia.uol.com.br/acoes-bovespa.html?exchangeCode=.BVSP&page=1&size=3000'

	page = requests.get(url)
	page.raise_for_status()
	cotacoes_soup = bs4.BeautifulSoup(page.text, "lxml")

	company_codes = cotacoes_soup.find_all(class_ = "clear-box")

	for code in company_codes:
		print code


con = None

try:
    con = lite.connect('test.db')
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data                
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()

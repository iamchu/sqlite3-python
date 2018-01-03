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


def tableConstructor(table_name):
	con = lite.connect('test.db')

	with con:
	    
	    cur = con.cursor()    
	    command_string_create = "CREATE TABLE "+ table_name +"(data TEXT, cotacao REAL, minima REAL, maxima REAL, variacao REAL, variacao_porcentagem REAL, volume INT)" 
	    command_string_insert = "INSERT INTO " + table_name + " VALUES('21/12/2017', 1231.12, 1000.12, 1300.14, 100.12, 10, 999111222)"
	    cur.execute(command_string_create)
	    cur.execute(command_string_insert)

tableConstructor("ITUB4_SA")


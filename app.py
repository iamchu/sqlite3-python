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

	# pessoas = (("joao",10, ""), 
	# 	("Maria", 20, "01/11/1990"),
	# 	("Alex", 30, "9/09/1980"))

	pessoas = []

	for i in range(2000):
		pessoas.append(["2 - 4" + str(i/20), i, str(i*10) ])	

	with con:
	    cur = con.cursor()    
	    cur.execute("DROP TABLE IF EXISTS people")
	    cur.execute("CREATE TABLE people(nome TEXT, idade REAL, aniversario TEXT)")
	    cur.executemany("INSERT INTO people VALUES(?,?,?)", pessoas)

tableConstructor("ITUB4_SA")


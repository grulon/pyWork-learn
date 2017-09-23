# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:32:33 2017

@author: glrulon
"""

import pyodbc

#MUST SET UP DB TABLE FIRST : MAKE SURE DATA TYPES ARE CORRECT OR YOU'LL GET ERRORS
cnxn = pyodbc.connect(driver='{SQL Server}', server='.', database='TestPython', uid='Python', pwd='asdf')
cursor = cnxn.cursor()

d = 5+2
a = 'nope'

cursor.execute("insert into testtable(id, name) values (?, ?)", d, a) 
cnxn.commit()

#https://geonet.esri.com/thread/64773
#https://code.google.com/p/pyodbc/wiki/GettingStarted
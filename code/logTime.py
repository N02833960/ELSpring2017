#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys
import datetime

def logTime():
 con = mydb.connect('testTime.db') #connect to DataBase
 with con: #open and close connection once done
		now = datetime.datetime.now() #give vari now the date and time
		timeString = now.strftime("%H-%M-%S") #format to display time
		timeString2 = now.strftime("%Y-%m-%d") #format to display date
		cur = con.cursor() #get connection curson
		#sql = "insert into tempData values(?,?)" #Format of entry
		cur.execute('insert into tempData values(?,?)',(timeString2,timeString)) #actual entry
		print "temp logged" #proof of logged

logTime() #call function


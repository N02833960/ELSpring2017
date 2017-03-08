#!/usr/bin/python
import os
import time
import csv

t_end = time.time() + 60 * 10
""" Log Current Time, Temperature in Celsius and Fahrenheit
        Returns a list [time, tempC, tempF] """
with open('loggerTemp.csv', 'w') as csvfile:    
 a = csv.writer(csvfile,delimiter= ",")
 data = ["Date&Time","Celsius","Fahrenheit"]
 a.writerow(data);
 while time.time() < t_end:
	def readTemp():
        	tempfile = open("/sys/bus/w1/devices/28-0516921f68ff/w1_slave")
       		tempfile_text = tempfile.read()
        	currentTime=time.strftime('%x %X %Z')
        	tempfile.close()
        	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
        	tempF=tempC*9.0/5.0+32.0
		data = [[currentTime, tempC, tempF]]
		a.writerows(data)
		return [currentTime, tempC, tempF]
	print readTemp()
	time.sleep(29)

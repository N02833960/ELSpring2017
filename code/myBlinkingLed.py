#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)
def Blink():
  for i in range(0,3):
	print "blink #" + str(i+1)
	GPIO.output(17,True)
	time.sleep(.5)
	GPIO.output(17,False)
	time.sleep(.5)
  print "Wait 5 Seconds"
  time.sleep(5)
  for i in range(0,4):
	 print "blinks2 #" + str(i+1)
	 GPIO.output(17,True)
	 time.sleep(.5)
 	 GPIO.output(17,False)
	 time.sleep(.5)
  print "Done!! Now Start Again "
  time.sleep(1)
  Blink()
  GPIO.cleanup()
Blink()

#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import sys
import MFRC522
import signal
import time
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD')
from Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD(pin_rs=20, pin_e=16, pins_db=[26, 19, 13, 6])
lcd.clear()
lcd.message('Tuer\ngeschlossen')

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.OUT)
#GPIO.setup(21, GPIO.OUT)
GPIO.output(4, True)


#Benutzer
RFID1 = '90145241197'
RFID2 = '63612518'
RFID3 = '1111'

#GPIO setup

continue_reading = True

def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

while continue_reading:

# Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Karte erkannt"

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

	 # Get UID
	UIDcode = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])      
#	print UIDcode 

	if UIDcode == RFID1:
		GPIO.output(4, False)
		print "Opened"
		lcd.clear()
		lcd.message('Hallo Andreas,\nTuer geoeffnet')
		time.sleep(3)
		GPIO.output(4, True)		
		print "Closed"
		lcd.clear()
		lcd.message('Tuer geschlossen')
        	time.sleep(0.2)
		
        if UIDcode == RFID2:
                GPIO.output(4, False)
                print "Opened"
                lcd.clear()
                lcd.message('Hallo Gunther,\nTuer geoeffnet')
                time.sleep(3)
                GPIO.output(4, True)
                print "Closed"
                lcd.clear()
                lcd.message('Tuer geschlossen')
		time.sleep(0.2)	

	else:
            print "Nicht erkannt"
	    lcd.message('Kein Zutritt')
	    time.sleep(1)
	    lcd.clear()

#try:
#	while True:
#		 if (GPIO.input(17)):
#                	print "Opened"
#                	lcd.clear()
#                	lcd.message('Tuer geoeffnet')
#	               	time.sleep(3)
#                	GPIO.output(4, True)
#                	print "Closed"
#                	lcd.clear()
#			lcd.message('Tuer gesclossen')




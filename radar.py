import subprocess
import os
import sys
import struct
import bluetooth._bluetooth as bluez
import bluetooth
import thread
import subprocess
import urllib2
import time
import re
import RPi.GPIO as GPIO
from twilio.rest import TwilioRestClient

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

distance = -1000
sell = True

def byte_to_signed_int(byte_):
    if byte_>127:
        return byte_ - 256
    else:
        return byte_


def checkDistance():
    global sell
    while True:
        res = subprocess.Popen('hcitool rssi "34:2D:0D:BF:5E:E6"', shell=True, stdout=subprocess.PIPE).stdout.read()

        p = re.compile('RSSI return value: (.*)')
        resArr = p.findall(res)

        if len(resArr) > 0:
            distance = int(resArr[0])
            print(distance)
            if distance < -30:
                if sell:
                    sell = False
                    contents = urllib2.urlopen("http://176.31.100.76:9999/item/SKU1000878/sell").read()

        time.sleep(1)

thread.start_new_thread(checkDistance, ())

while True:
    continue

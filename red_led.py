#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ledPin = 13

GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, GPIO.HIGH)
time.sleep(10)
GPIO.output(ledPin, GPIO.LOW)

GPIO.cleanup()

#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

relayPin = 16

GPIO.setup(relayPin, GPIO.OUT)

time.sleep(10)
GPIO.output(relayPin, GPIO.HIGH)
time.sleep(10)
GPIO.output(relayPin, GPIO.LOW)

GPIO.cleanup()

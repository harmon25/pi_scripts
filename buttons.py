#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    orange_state = GPIO.input(5)
    if orange_state == False:
        print('Orange Button Pressed')
        time.sleep(0.2)
    blue_state = GPIO.input(6)
    if blue_state == False:
        print('Blue Button Pressed')
        time.sleep(0.2)
    green_state = GPIO.input(13)
    if green_state == False:
        print('Green Button Pressed')
        time.sleep(0.2)

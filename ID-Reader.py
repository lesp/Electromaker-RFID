#!/usr/bin/env python3

import RPi.GPIO as GPIO
import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522.SimpleMFRC522()
file = open("ID.txt", "a")
print("Hold a tag near the reader")

try:
    while True:
        id, text = reader.read()
        print(id)
        #print(text)
        file.write(str(id)+"\n")
        sleep(1)
finally:
    print("cleaning up")
    GPIO.cleanup()
    file.close()

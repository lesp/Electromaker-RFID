import RPi.GPIO as GPIO
import SimpleMFRC522
from time import sleep
import subprocess
import webbrowser


def slow_type(message):
    for character in message:
        print(character, end="")
        sleep(0.01)
    print("\n")
        

reader = SimpleMFRC522.SimpleMFRC522()

slow_type("Electromaker RFID User Interface V1.0\n********************\nHold a tag near the reader to start an application\n")

try:
    while True:
        id, text = reader.read()
        #print(id)
        sleep(0.1)
        if id == 629717360455:
            slow_type("Create documents with Libreoffice")
            subprocess.call(["libreoffice"])
            sleep(0.2)
        elif id == 572050203913:
            slow_type("Opening web browser")
            webbrowser.open_new("https://www.electromaker.io/")
            sleep(0.2)
        elif id == 866687919239:
            slow_type("Opening Task Manager")
            subprocess.call(["lxtask"])
            sleep(0.2)
except KeyboardInterrupt:
    slow_type("Exiting the application, bye!")
    GPIO.cleanup()

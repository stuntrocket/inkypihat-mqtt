import paho.mqtt.client as mqtt
import os
import logging
import time

from inky_screen import InkyScreen
client = mqtt.Client()

myScreen = InkyScreen()
client = mqtt.Client()

# myScreen.message("Please Wait", 'red')
# time.sleep(1)
# myScreen.message("Connecting", 'white')
# time.sleep(1)
# myScreen.message("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 'white')
myScreen.down_alert("GINACAMPBELL | DOWN @ | 2021-05-07 11:12:04")

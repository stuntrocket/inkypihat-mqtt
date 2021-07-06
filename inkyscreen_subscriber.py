import paho.mqtt.client as mqtt
import os
import logging
import time

from inky_screen import InkyScreen
from pizero_screen_config import pizero_screen_config

logging.basicConfig(filename='/tmp/debug.log', level=logging.DEBUG)

MQTT_BROKER = pizero_screen_config["mqtt_broker"]
MQTT_TOPIC = pizero_screen_config["mqtt_topic"]
MQTT_PORT = pizero_screen_config["mqtt_port"]

myScreen = InkyScreen()
client = mqtt.Client()

myScreen.message("Initialising...", 'white')

def on_connect(client, userdata, flags, rc):
    # logger.info("Connected with result code " + str(rc))
    myScreen.message('Connected.', 'white')
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    m = msg.payload.decode('utf-8')
    bg = 'white'
    
    if "DOWN @" in m:
        bg = 'red'
        myScreen.down_alert(m, bg)
    elif "REBOOT" in m:
        bg = 'black'
        myScreen.message('REBOOT', bg)
        time.sleep(5)
        os.system("sudo systemctl reboot -i")
    elif "SHUTDOWN" in m:
        bg = 'black'
        myScreen.message('SHUTDOWN', bg)
        time.sleep(5)
        os.system("sudo shutdown -h now")
    else:
        myScreen.message(m, bg)


client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_forever()

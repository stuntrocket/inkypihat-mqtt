# InkyPiHat MQTT Notifier

Listen for messages on MQTT broker and then display message on Inky PiHat screen.

Requires an MQTT broker.

## Installation

> (update paths to match your system)

```
mkdir -p /home/pi/code
git clone https://github.com/stuntrocket/inkypihat-mqtt.git inkypihat
```

```sudo vim /etc/systemd/system/inkyscreen.service```

```
[Unit]
Description=MQTT Client Inky Service
After=multi-user.target
Requires=network.target

[Service]
Type=idle
User=root
ConditionPathExists=!/home/pi/code/inkypihat/lockfile
ExecStartPre=/bin/touch /home/pi/code/inkypihat/lockfile
ExecStart=/usr/bin/python3 /home/pi/code/inkypihat/inkyscreen_subscriber.py
ExecStopPost=/bin/rm -f /home/pi/code/inkypihat/lockfile
Restart=on-failure
RestartSec=60

[Install]
WantedBy=multi-user.target
```

```sudo chmod 644 /etc/systemd/system/inkyscreen.service```

```sudo systemctl daemon-reload```

```sudo systemctl enable inkyscreen```

```sudo systemctl start inkyscreen```


## Config

In the config file, set the topic that the broker is listening to.

> pizero_screen_config.py

```
pizero_screen_config = {
'mqtt_broker': 'naspi.local',
'mqtt_port': 1883,
'mqtt_topic': 'house/notify/#'
}
```


## Other Commands

```sudo systemctl restart inkyscreen```

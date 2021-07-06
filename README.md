113  cd code/mqtt_spl_screen/
114  python3 pizero_screen_subscriber.py 
115  sudo python3 pizero_screen_subscriber.py 
116  sudo apt-get install supervisor
117  sudo vim /etc/systemd/system/screen.service
118  sudo chmod 644 /etc/systemd/system/screen.service
119  sudo systemctl daemon-reload
120  sudo systemctl enable screen
121  sudo systemctl start screen
122  ls -la /home/pi/code/mqtt_spl_screen
123  sudo vim /etc/systemd/system/screen.service
124  sudo systemctl restart screen
125  sudo systemctl daemon-reload
126  sudo systemctl restart screen

Updated...
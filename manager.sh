#!/bin/bash

export FLASK_APP=server
#rm arduinoData.csv
python3 listen.py
flask run --host=192.168.1.6
echo "ran listener and Listener"

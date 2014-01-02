#!/bin/bash

CONFIG="config.py"

if [ -f $CONFIG ]
then
    echo "Config file found. Starting..."
    python3 lykos.py
else
    echo "============================="
    echo "==  _       _              =="
    echo "== | |     | |             =="
    echo "== | |_   _| | _____  ___  =="
    echo "== | | | | | |/ / _ \/ __| =="
    echo "== | | |_| |   < (_) \__ \ =="
    echo "== |_|\__, |_|\_\___/|___/ =="
    echo "==     __/ |               =="
    echo "==    |___/                =="
    echo "============================="
    echo "== Welcome to lykos!       =="
    echo "== Setup is simple. I'm    =="
    echo "== copying a sample config =="
    echo "== file to config.py.      =="
    echo "== Modify that (the        =="
    echo "== settings are pretty     =="
    echo "== self-explanatory) and   =="
    echo "== run this script again.  =="
    echo "== Have fun with your new  =="
    echo "== wolfbot!                =="
    echo "============================="
    cp sample_config.py config.py
fi

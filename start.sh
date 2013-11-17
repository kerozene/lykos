#!/bin/bash

CONFIG="lykos.cfg"

if [ -f $CONFIG ]
then
    echo "Config file found. Starting..."
    source lykos.cfg
    python3 lykos.py $LYKOS_NETWORK $LYKOS_CHANNELS $LYKOS_NAME
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
    echo "== file to lykos.cfg.      =="
    echo "== Modify that (the        =="
    echo "== settings are pretty     =="
    echo "== self-explanatory) and   =="
    echo "== run this script again.  =="
    echo "== Have fun with your new  =="
    echo "== wolfbot!                =="
    echo "============================="
    cp lykos_sample.cfg lykos.cfg
fi

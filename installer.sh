#! /bin/bash
cd /home/pi
sudo apt update
sudo apt install python3-dev
git clone https://github.com/simonmonk/SPI-Py.git
cd SPI-Py
sudo python3 setup.py install
wget https://raw.githubusercontent.com/simonmonk/clever_card_kit/master/SimpleMFRC522.py
wget https://raw.githubusercontent.com/simonmonk/clever_card_kit/master/MFRC522.py

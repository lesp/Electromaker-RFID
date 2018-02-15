![alt](https://www.electromaker.io/images/base/electromaker-logo.jpg)
# Electromaker RFID Application Interface

Start applications on your Raspberry Pi using nothing more than RFID tags / cards.

## Getting Started

Download the code for this project and extract to your ```/home/pi``` directory.
Run the ```installer.sh``` from the terminal as follows.

```
cd Electromaker-RFID
./installer.sh
```

### Contents of the Installer

```
#! /bin/bash
cd /home/pi
sudo apt update
sudo apt install python3-dev
git clone https://github.com/simonmonk/SPI-Py.git
cd SPI-Py
sudo python3 setup.py install
cd /usr/local/lib/python3.5/dist-packages
sudo wget https://raw.githubusercontent.com/simonmonk/clever_card_kit/master/SimpleMFRC522.py
sudo wget https://raw.githubusercontent.com/simonmonk/clever_card_kit/master/MFRC522.py
```

## Circuit Diagram

![alt](https://raw.githubusercontent.com/lesp/Electromaker-RFID/master/RFID-Circuit_bb.png)

## Acknowledgements

* [SPI-Py](https://github.com/simonmonk/SPI-Py) - Hardware SPI C extension for Python from Simon Monk
* [SimpleMFRC522 and MFRC522 Python libraries](https://github.com/simonmonk/clever_card_kit) Also from Simon Monk

[Go and buy Simon's clever card kit, it is great!](https://www.monkmakes.com/cck/)


## License

This project is licensed under the MIT License.


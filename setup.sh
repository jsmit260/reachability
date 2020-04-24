#! /bin/bash

apt update
apt install -y python3.8
apt install -y python3-pip
pip3 install python-masscan
pip3 install tabulate
pip install ipaddress
sed -i 's/logger.debug/#&/' $(locate masscan.py)

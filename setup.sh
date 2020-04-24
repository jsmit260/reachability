#! /bin/bash

apt update
apt install -y python3.8
apt install -y python3-pip
python3 -m pip install --upgrade pip setuptools
pip3 install python-masscan
pip3 install tabulate
pip install ipaddress
sed -i 's/logger.debug/#&/' $(locate masscan.py)

# -- START DISCLAIMER --

# USE AT OWN RISK -- IN NO WAY AM I RESPONSIBLE FOR ANY DAMAGES INCURRED -- IF YOU DON'T HAVE EXPLICT PERMISSION BY THE NETWORK OWNER DO NOT AND I REPEAT DO NOT LAUNCH THIS 

THIS IS PYTHON WRAPPED AROUND MASSCAN (https://github.com/robertdavidgraham/masscan)
# -- END DISCLAIMER--

These scripts assume you are on a debian linux distro and have internet access.

If running in a VMware Virtual Machine, make sure you are using a bridged interace. Do not use a VMware NAT interface as when tested it crashes the virutal NAT even with slow pps as low as 1,000.

Are the target ranges reachable?

# reachy.py
This answers....Are the target ranges reachable?

# EASYMODE - COPY/PASTA (into your terminal):
[WARNING : DO NOT RUN ON A CORP Attached Network unless you are meaning too. ]
This command will download the tool, set it up, and run it on the first network interface you are attached to as a /24.
> sudo git clone https://github.com/jsmit260/reachability.git && cd reachability&&sudo chmod 755 setup.sh && ./setup.sh && ifconfig | grep 'inet ' | grep -v 127 | cut -d ' ' -f 10 | cut -d '.' -f 1,2,3 > targets.list >> targets.list && sed -i '1s/.*/&.0\\/24/' targets.list && sudo ./reachy.py targets.list

# MANUAL MODE:

>sudo git clone https://github.com/jsmit260/reachability.git

>cd reachability

>sudo chmod 755 setup.sh

> sudo ./setup.sh

(This script makes sure you have everything you need to run fast-portsweep.py)

Create a line seperated list of target IP Ranges (IE: x.x.x.x/24).
> echo "127.0.0.1/32" >> targets.list
> echo "192.168.1.1/32" >> targets.list

Fire at will:
>sudo ./reachy.py targets.list




# FOLLOW THE DOGE TO WATCH THE DEMO (click on the dog)
[![Watch the video](https://i.imgur.com/EVvpwLb.jpg)](https://youtu.be/VHPm6h8ZAeM)




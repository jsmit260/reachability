# -- START DISCLAIMER --

# USE AT OWN RISK -- IN NO WAY AM I RESPONSIBLE FOR ANY DAMAGES INCURRED -- IF YOU DON'T HAVE EXPLICT PERMISSION BY THE NETWORK OWNER DO NOT AND I REPEAT DO NOT LAUNCH THIS 

THIS IS PYTHON WRAPPED AROUND MASSCAN (https://github.com/robertdavidgraham/masscan)
# -- END DISCLAIMER--

These scripts assume you are on a debian linux distro and have internet access.

Are the target ranges reachable?

# reachy.py
This answers....Are the target ranges reachable?

# EASYMODE - COPY/PASTA (into your terminal):
[WARNING : DO NOT RUN ON A CORP Attached Network unless you are meaning too. ]
This command will download the tool, set it up, and run it on the first network interface you are attached to as a /24.
> sudo git clone https://github.com/jsmit260/reachability.git && cd reachability&&sudo chmod 755 setup.sh && sudo ./setup.sh && echo ' ' && echo ' '&& echo '**Create a file named targets.list or whatever, fill it with line seperate IP ranges in CIDR notation such as 192.168.0.0/24 then run $>./ireach.py to continue life on easy street**'

# MANUAL MODE:

>sudo git clone https://github.com/jsmit260/reachability.git

>cd reachability

>sudo chmod 755 setup.sh

> sudo ./setup.sh

(This script makes sure you have everything you need to run reachy.py)

Create a line seperated list of target IP Ranges (IE: x.x.x.x/24).
> echo "127.0.0.1/32" >> targets.list
> echo "192.168.1.1/32" >> targets.list

Fire at will:
>sudo ./reachy.py targets.list




# FOLLOW THE DOGE TO WATCH THE DEMO (click on the dog)
[![Watch the video](https://i.imgur.com/EVvpwLb.jpg)](https://youtu.be/VHPm6h8ZAeM)




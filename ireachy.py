#! /usr/bin/python3

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
import os
questions = [
    {
        'type': 'input',
        'name': 'ranges_to_scan',
        'message': 'What file contians your list of ranges?',
    },
    {
        'type':'list',
        'name':'speed_to_scan',
        'message':'How Fast? (Packets Per Seconds)',
        'choices':['100','1000','10000','100000','200000'],
        'filter':lambda val: val.lower()
    }
]

answers = prompt(questions)
pprint(answers)  # use the answers as input for your app

command2run='python3 reachy.py '+answers['ranges_to_scan']+' '+answers['speed_to_scan']
os.system(command2run)


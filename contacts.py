# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:02:26 2018

@author: Anonymousgod
"""

import csv
import random
with open('contacts.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    readerr =  list(csvfile)
    print random.choice(readerr)
        
    
print raw_input("press the enter key to exit")

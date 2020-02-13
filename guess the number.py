# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:20:14 2020

@author: USER
"""

import random
a=random.randint (1,10)
while True:
    b=input("Guess a number:")
    if int(b) == a:
        print("Correct!")
        break
    else:
        print("Try again!")
        
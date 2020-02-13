# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:12:54 2020

@author: USER
"""

import random
a=random.randint (1,20)
print("You have 5 tries. START!") 

i=1
while i<6:
    b=input("Guess a number from 1 to 20 :")
    if int(b)==a:
        print("Well Done! You have already tried",i,"time[s]!")
        break
    elif int(b)<a:
        print("Guess a bigger number!","You have already tried",i,"time[s]!")
    elif int(b)>a:
        print("Guess a smaller number!","You have already tried",i,"time[s]!")
    i=i+1
if i==6:
    print("Game Over!")
    
            
            
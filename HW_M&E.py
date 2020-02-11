# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:38:45 2020

@author: USER
"""

MS=input("Enter your math score:")
LAS=input("Enter your L.A. score:")
if int(MS)>=90 and int(LAS)>=90: 
    print("You win a prize!")
elif int(MS)<60 and int(LAS)<60:
    print("You fail!")
elif int(MS)<60 or int(LAS)<60:
    print("Keep trying!")
else:
    print("Not bad!")
         
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:54:43 2020

@author: USER
"""

W=input("Enter Weight:")
H=input("Enter Hieght:")
BMI=float(W)//(float(H)*float(H))
print("BMI="+str(BMI))
if BMI<=18.5:
    print("overlight")
elif BMI>24:
    print("overwieght")
else:
    print("normal")
    
    
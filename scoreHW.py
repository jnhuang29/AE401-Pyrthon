# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:46:04 2020

@author: USER
"""
scorelist=[]
namelist=[]
highest=0
lowest=100
classmates=input('How many classmates are in your class?')
for i in range(int(classmates)):
    names=input('Student name:')
    score=input("What was your score?")
    scorelist.append(int(score))
    namelist.append(names)
    if int(score)>highest:
        highest=int(score)
        topname=names
    elif int(score)<lowest:
        lowest=int(score)
        bottomname=names
average=sum(scorelist)/(int(classmates))
print('Your class average is:',average)
print("Your class's highest score is:",topname,highest)
print("your class's lowest score is:",bottomname,lowest)

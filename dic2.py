# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:04:09 2020

@author: USER
"""

dic={}
how_many=int(input('How many vocab words and values are you going to write?'))
for i in range(how_many):
    vocab=('Insert your vocabulary word:')
    meaning=('What is the meaning?')
    dic[vocab]=meaning

for k, v in dic.items():
    print(k, v)
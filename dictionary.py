# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:12:21 2020

@author: USER
"""

dic={'dog':5,'cat':12,'snake':16}
dic['turtle']=19
dic.pop('snake')
print(dic)
for key in dic.keys():
    print(key)
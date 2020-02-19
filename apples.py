# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:03:38 2020

@author: USER
"""
apple_num=0
each_price=0
purchased_apples=0
sold_apples=0
money_earned=0
list_sold=[]
while True:
    boss=int(input('Select a number:'))
    if boss==1:
        apple_num=int(input('How many apples do you have in storage?'))
        each_price=int(input('How much money does it cost?'))
        print(apple_num,each_price)
    elif boss==2:
        purchased_apples=int(input('How many apples have you purchased today?'))
        apple_num=apple_num+purchased_apples
        print(purchased_apples)
    elif boss==3:
        sold_apples=int(input('How many apples have you sold today?'))
        apple_num=apple_num-sold_apples
        list_sold.append(sold_apples)
        print(sold_apples)
    elif boss==4:
        list_sold=
        print(list_sold)
    elif boss==5:
        print(apple_num)
    elif boss==6:
        break
    else:
        print('No function.')
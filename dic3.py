# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:39:20 2020

@author: USER
"""
dic={}
while True:
    print('1=create.2=list or print.3=english converted into chinese.4=chinese to english.5=test.6=exit.')
    choice=int(input('Select a number:'))
    if choice==1:
        new_words=input("New words:")
        chinese=input('Chinese words:')
        dic[new_words]=chinese
        doc=open('L9test.txt','w')
        doc.write('Close')
        doc=open('L9test.txt','r')
        print(doc.read)
        doc=open('L9test.txt','a')
        doc.write('And reopen')
        doc.close()
    elif choice==2:
        for key,value in dic.items():
            print(key,value)
    elif choice==3:
        search_eng=input('Search for an english word:')
        for key in dic.keys():
            #print(key, dic[key])
            if search_eng==key:
                print(key, dic[key])
    elif choice==4:
        search_chi=input('Search for a chinese word.')
        
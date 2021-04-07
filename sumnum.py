# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:20:28 2021

@author: new
"""

"""ty_num = input('Type your number: ')
num = int(ty_num)"""
def sumAll(num):
        i = 1
        sum = 0
        while i <= num:
            sum = sum + i
            i = i + 1
        print(sum) 
        
def evenNum(num):
        i = 2
        sum = 0
        while i <= num:
            sum = sum + i
            i = i + 2
        print(sum) 

def oddNum(num):
        i = 1
        sum = 0
        while i <= num:
            sum = sum + i
            i = i + 2
        print(sum) 
        
sumAll(10)
evenNum(10)
oddNum(10)



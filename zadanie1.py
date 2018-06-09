# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:25:01 2018

@author: Tom
"""

x=input("Enter postal code lower bound: ")
y=input("Enter postal code upper bound: ")

def postal(x,y):
    x1=int(str(x[0]+x[1]+x[3]+x[4]+x[5]))
    y1=int(str(y[0]+y[1]+y[3]+y[4]+y[5]))
    for i in range(x1+1,y1):
        result=str(i)
        print(result[0:2]+"-"+result[2:5])
        
postal(x,y)      

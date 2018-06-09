# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:55:29 2018

@author: Tom
"""

from decimal import Decimal

def decimal_gen():
    
    i=Decimal('1.5')
    a=Decimal('0.5')
    while True:
   
        i+=a
        print(i)
        if i==5.5:
            break
    
decimal_gen()








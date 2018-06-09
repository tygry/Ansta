# -*- coding: utf-8 -*-


"""
Wejscie: lista w postaci [x,y,z,...,n] i liczba dodatnia 
oddzielone od siebie srednikiem (;)
Wyjscie: roznica miedzy lista generowana na podstawie liczby i lista wejsciowa
"""

def dif(): 
    
    user_list, n =input("Enter list ([x,y,z,...,n]) and number separated by semicolon: ").split(';')
    n=int(n)
    reference_list=list(range(1, n+1)) #utworzenie listy od 1 do n
    
    for x in user_list: #zastepowanie zbednych znakow spacjami
        if "," in user_list:
            user_list=user_list.replace(',',' ')
        if "[" in user_list:
            user_list=user_list.replace('[',' ')
        if "]" in user_list:
            user_list=user_list.replace(']',' ')
                
    user_integer_list = map(int, user_list.split()) #zamiana elementow stringa oddzielonych spacjami na wartosci int
    
    user_integer_list=list(user_integer_list) 
    result_list=(list(set(reference_list)-set(user_integer_list))) #odejmowanie setow
    result_list.sort() #uporzadkowanie rosnaco
    print(result_list)
   
dif() 



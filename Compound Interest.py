# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 08:03:13 2021

@author: HP
"""
#Compound Interest
#A= P(1 + R/100) t 

def compound_interest(p,r,t):
    A=p*pow(1+(r/100),t)
    return A
p=4000
r=12.5
t=2.3
print("Compound Amount is ",compound_interest(p, r, t))

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 07:51:08 2021

@author: HP
"""

def factorilal(n):
    return 1 if(n==1 or n==0) else n*factorilal(n-1)
n=5
print("The factorial of ",n,"is",factorilal(n))

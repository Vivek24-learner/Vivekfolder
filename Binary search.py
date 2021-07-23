# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 04:00:05 2021

@author: HP
"""
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while low<=high:
        low=(mid+high)
        if(arr[mid]<x):
            low=mid+1    
        elif(arr[mid]>1):
            high=mid-1
        else:
            return mid
    return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
        
  
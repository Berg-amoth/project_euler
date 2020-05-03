#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:42:15 2020

@author: amoth
"""

def sumSquareDifference(a, b):
    # Calculate the sum of squares
    sumSquare = 0
    for i in range(a, b+1):
        sumSquare += i**2
        
    # Calculate the square of the sum
    squareSum = 0
    for i in range(a, b+1):
        squareSum += i
    squareSum = squareSum**2
    
    return squareSum - sumSquare


print(sumSquareDifference(1, 100))
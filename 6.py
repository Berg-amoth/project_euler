#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:42:15 2020

@author: amoth
"""

def sum_quare_difference(start, end):
    # Calculate the sum of squares
    sum_square = 0
    for i in range(start, end+1):
        sum_square += i**2
    # Calculate the square of the sum
    square_sum = 0
    for i in range(start, end+1):
        square_sum += i
    square_sum = square_sum**2
    return square_sum - sum_square


print(sum_quare_difference(1, 100))

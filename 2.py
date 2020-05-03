#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:29:19 2020

@author: amoth
"""

import math as m

def evenFibonacciNumbers(i, o, max):
    sum = 0
    while i < max:
        if i/2 == m.floor(i/2):
            sum += i
        i, o = o, o + i
    return sum

print(evenFibonacciNumbers(1, 2, 4000000))
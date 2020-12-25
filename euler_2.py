#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:29:19 2020

@author: amoth
"""

import math as m

def even_fibonacci_numbers(i, o, maximum):
    summ = 0
    while i < maximum:
        if i/2 == m.floor(i/2):
            summ += i
        i, o = o, o + i
    return summ

print(even_fibonacci_numbers(1, 2, 4000000))

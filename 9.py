#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:37:03 2020

@author: amoth
"""

import math as m

# a < b < c < x/2 < a+b
# a + b + c = 1000
# return 0 if no result
def pythagorean_triplet(x):
    # c and b starting at their maximum while a initiate at minimum
    c = m.floor(x/2)
    b = c - 1
    a = x - c - b
    while a**2 + b**2 != c**2:
        if b <= a:
            c -= 1
            b = c - 1
            a = x - c - b
            if c < 2:
                c = 0
                b = 0
                a = 0
        else:
            b -= 1
            a += 1
    return a*b*c


print(pythagorean_triplet(1001))

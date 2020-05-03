#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:16:46 2020

@author: amoth
"""

import math as m

def multiplesBelowN(n):
    sum = 0
    for i in range(3, n):
        if (i/3 == m.floor(i/3)) | (i/5 == m.floor(i/5)):
            sum += i
    
    return sum

print(multiplesBelowN(1000))
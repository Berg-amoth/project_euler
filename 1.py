#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:16:46 2020

@author: amoth
"""

import math as m

def sum_multiples_below(maximum):
    sum_of_multiples = 0
    for i in range(3, maximum):
        if (i/3 == m.floor(i/3)) | (i/5 == m.floor(i/5)):
            sum_of_multiples += i
    return sum_of_multiples

print(sum_multiples_below(1000))

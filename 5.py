#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:54:52 2020

@author: amoth
"""

def smallestMultiple(a, b):
    SM = 0
    test = b
    while SM == 0:
        countMultiples = 0
        for i in range(a, b+1):
            if (test%i) == 0:
                countMultiples += 1
                
        if countMultiples == (b-a+1):
            SM = test
        else:
            test += b
    return SM


print(smallestMultiple(1, 20))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:54:52 2020

@author: amoth
"""

def smallest_multiple(start, end):
    smal_mult = 0
    test = end
    while smal_mult == 0:
        count_multiples = 0
        for i in range(start, end+1):
            if (test%i) == 0:
                count_multiples += 1                
        if count_multiples == (end-start+1):
            smal_mult = test
        else:
            test += end
    return smal_mult


print(smallest_multiple(1, 20))

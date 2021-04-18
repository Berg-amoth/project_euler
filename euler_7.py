#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:56:31 2020

@author: amoth
"""

import lib.m_utils as mu


def umpteenth_prime_number(row):
    if row == 1:
        tested_number = 2
    elif row == 2:
        tested_number = 3
    # If row > 2, tested_number can be incremented by 2
    else:
        counter = 3
        tested_number = 3
        # Each time tested_number is a prime number, counter is incremented
        while counter <= row:
            tested_number += 2
            if mu.is_prime(tested_number):
                counter += 1
    return tested_number


print(umpteenth_prime_number(10001))

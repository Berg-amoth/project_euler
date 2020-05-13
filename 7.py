#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:56:31 2020

@author: amoth
"""

import math as m


def is_prime(number):
    is_that_number_prime = True
    # Si non entier : non premier
    if number != m.floor(number):
        is_that_number_prime = False
    # On divise number par tous les nombres inférieurs à sa racine
    divider = m.floor(m.sqrt(number))
    while (divider > 1) & is_that_number_prime:
        if (number/divider) == (m.floor(number/divider)):
            is_that_number_prime = False
        divider -= 1
    return is_that_number_prime


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
            if is_prime(tested_number):
                counter += 1
    return tested_number


print(umpteenth_prime_number(10001))

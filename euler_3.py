#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:36:41 2020

@author: amoth
"""

import math as m

import lib.m_utils as mu


def find_largest_prime_factor(number):
    largest_prime_factor = 1
    divider = m.floor(m.sqrt(number))
    if divider/2 == m.floor(divider/2):
        divider -= 1
    while (divider >= 3) & (largest_prime_factor == 1):
        if number/divider == m.floor(number/divider):
            if mu.is_prime(divider):
                largest_prime_factor = divider
        divider -= 2
    if (largest_prime_factor == 1) & (number/2 == m.floor(number/2)):
        largest_prime_factor = 2
    return largest_prime_factor


print(find_largest_prime_factor(600851475143))

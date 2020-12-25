#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:36:41 2020

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


def find_largest_prime_factor(number):
    largest_prime_factor = 1
    divider = m.floor(m.sqrt(number))
    if divider/2 == m.floor(divider/2):
        divider -= 1
    while (divider >= 3) & (largest_prime_factor == 1):
        if number/divider == m.floor(number/divider):
            if is_prime(divider):
                largest_prime_factor = divider
        divider -= 2
    if (largest_prime_factor == 1) & (number/2 == m.floor(number/2)):
        largest_prime_factor = 2
    return largest_prime_factor


print(find_largest_prime_factor(600851475143))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:50:43 2020

@author: amoth
"""

import math as m

def is_palindrome(number):
    temp = number
    number_digits = 0
    # Calcule le nombre de digits de number
    while temp > 0:
        if m.floor(temp/10) > 0:
            number_digits += 1
        temp = m.floor(temp/10)
    # On regarde si les extrêmes sont égaux : on les supprimes : on arrête
    while number_digits >= 0:
        if (number // 10**number_digits) == (number % 10):
            number = m.floor((number - (number//10**number_digits)*10**number_digits)/10)
            number_digits -= 2
        else:
            number_digits = -1
    return m.floor(number) == 0


def largest_palindrome_n_digits(number):
    largest_palindrome = 10**(number-1) + 1
    product_one = 10**number - 1
    minimum = 10**(number-1)
    while product_one >= minimum:
        product_two = product_one
        while product_two >= minimum:
            if is_palindrome(product_one*product_two) & (product_one*product_two > largest_palindrome):
                largest_palindrome = product_one*product_two
            product_two -= 1
        product_one -= 1
    return largest_palindrome


print(largest_palindrome_n_digits(3))

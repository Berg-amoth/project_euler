#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:50:43 2020

@author: amoth
"""

import lib.m_utils as mu


def largest_palindrome_n_digits(number):
    largest_palindrome = 10**(number-1) + 1
    product_one = 10**number - 1
    minimum = 10**(number-1)
    while product_one >= minimum:
        product_two = product_one
        while product_two >= minimum:
            if mu.is_palindrome(product_one*product_two) & (product_one*product_two > largest_palindrome):
                largest_palindrome = product_one*product_two
            product_two -= 1
        product_one -= 1
    return largest_palindrome


print(largest_palindrome_n_digits(3))

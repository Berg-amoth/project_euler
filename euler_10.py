#!/usr/bin/python3
# -*- coding:utf-8 -*-

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

def sum_primes(n):
    sum_primes_below_n = 2
    for i in range(3,n,2):
        if is_prime(i):
            print(i)
            sum_primes_below_n += i
    return sum_primes_below_n

print(sum_primes(2000000))

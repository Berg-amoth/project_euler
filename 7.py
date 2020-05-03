#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:56:31 2020

@author: amoth
"""

import math as m


def isPrime(n):
    isPrime = True
    # Si non entier : non premier
    if n != m.floor(n):
        isPrime = False
    # On divise n par tous les nombres inférieurs à sa racine
    a = m.floor(m.sqrt(n))
    while (a > 1) & isPrime:
        if (n/a) == (m.floor(n/a)):
            isPrime = False
        a -= 1
    return isPrime


def nPrime(n):
    if n == 1:
        nPrime = 2
    elif n == 2:
        nPrime = 3
    # If n > 2, nPrime can be incremented by 2
    else:
        counter = 3
        nPrime = 3
        # Each time nPrime is a prime number, counter is incremented
        while counter <= n:
            nPrime += 2
            if isPrime(nPrime):
                counter += 1                
    return nPrime


print(nPrime(10001))
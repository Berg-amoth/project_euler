#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:36:41 2020

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


def largestPrimeFactor(n):
    LPF = 1
    a = m.floor(m.sqrt(n))
    
    if a/2 == m.floor(a/2):
        a -= 1
        
    while (a >= 3) & (LPF == 1):
        if n/a == m.floor(n/a):
            if isPrime(a):
                LPF = a
        a -= 2
    
    if (LPF == 1) & (n/2 == m.floor(n/2)):
        LPF = 2
    
    return LPF


print(largestPrimeFactor(600851475143))
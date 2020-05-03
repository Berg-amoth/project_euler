#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:50:43 2020

@author: amoth
"""

import math as m

def isPalindrome(n):
    temp = n
    a = 0
    # Calcule le nombre de digits de n
    while temp > 0:
        if m.floor(temp/10) > 0:
            a += 1
        temp = m.floor(temp/10)
    # On regarde si les extrêmes sont égaux : on les supprimes : on arrête
    while a >= 0:
        if (n // 10**a) == (n % 10):
            n = m.floor((n - (n//10**a)*10**a)/10)
            a -= 2
        else:
            a = -1
    
    return m.floor(n) == 0   
    

def largestPalindromeNDigits(n):
    LPND = 10**(n-1) + 1
    a = 10**n - 1
    min = 10**(n-1)
    while (a >= min):
        b = a
        while (b >= min):
            if isPalindrome(a*b) & (a*b > LPND):
                LPND = a*b
            b -= 1
        a -= 1
    return LPND


print(largestPalindromeNDigits(3))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 15:18:39 2021

@author: pouja
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

def parse_int(string):
    liste = []
    for i in string:
        liste.append(int(i))
    return liste

def grid_to_lists(grid, n, m):
    listed_values = list()

    for i in range(n):
        temp_list = list()
        for o in range(i*3*m,i*3*m+3*m-1,3):
            temp_list.append(int(grid[o])*10+int(grid[o+1]))
        listed_values.append(temp_list)

    return listed_values
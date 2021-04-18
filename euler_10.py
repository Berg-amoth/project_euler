#!/usr/bin/python3
# -*- coding:utf-8 -*-

import lib.m_utils as mu

def sum_primes(n):
    sum_primes_below_n = 2
    for i in range(3,n,2):
        if mu.is_prime(i):
            print(i)
            sum_primes_below_n += i
    return sum_primes_below_n

print(sum_primes(2000000))

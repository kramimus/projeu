#!/usr/bin/env python

f_cache = {0: 0, 1: 1}

def fib(n):
    f_sum = f_cache[n - 1] + f_cache[n - 2]
    f_cache[n] = f_sum
    return f_sum

current_f = 0
f_n = 2
while len(str(fib(f_n))) < 1000:
    f_n += 1

print f_n

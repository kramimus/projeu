#!/usr/bin/env python

import math

base = 10
modulus = int(1e6) - 1
digits_available = range(base)

perm = []
for place in range(base - 1, -1, -1):
    x = math.factorial(place)
    digit = modulus / x
    modulus %= x
    perm.append(digits_available[digit])
    del digits_available[digit]

print ''.join(map(str, perm))

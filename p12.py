#!/usr/bin/env python

from collections import Counter
import math
import factoring
from operator import mul

def get_factor_count(n):
    prime_factors = factoring.get_prime_factors(n)

    prime_count = Counter(prime_factors)
    return reduce(mul, (i + 1 for i in prime_count.values()), 1)

if __name__ == '__main__':
    current_tri = 0
    for i in range(1, 100000):
        current_tri += i
        fac_count = get_factor_count(current_tri)
        print current_tri, fac_count
        if fac_count > 500:
            print current_tri, fac_count
            break

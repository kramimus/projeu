#!/usr/bin/env python

from collections import Counter
import math
from operator import mul

def get_prime_factors(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return [i] + get_prime_factors(n / i)
    else:
        return [n]
    return factors

def get_factor_count(n):
    prime_factors = get_prime_factors(n)

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

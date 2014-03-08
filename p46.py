#!/usr/bin/env python3

import itertools
import math
import prime

primes = None
ordered_primes = []
max_prime = 0

def is_composite(n):
    global primes
    global ordered_primes
    global max_prime
    if n <= max_prime:
        return n not in primes
    elif prime.is_prime(n):
        primes.add(n)
        ordered_primes.append(n)
        max_prime = n
        return False
    else:
        return True

def get_residuals(n):
    res = []
    for p in ordered_primes:
        if p >= n:
            break
        res.append(n - p)
    return res

def get_least_violation():
    global primes
    primes = prime.get_primes_up_to(int(1e6))
    for i in itertools.count(start=1, step=2):
        if is_composite(i):
            for residual in get_residuals(i):
                if residual / 2 == residual // 2:
                    sq = math.sqrt(residual // 2)
                    if math.floor(sq) == sq:
                        break
            else:
                return i

if __name__ == '__main__':
    print(get_least_violation())

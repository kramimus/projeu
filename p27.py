#!/usr/bin/etc python

import prime

def get_max_prime(a, b):
    n = 0
    still_prime = True
    while prime.is_prime(abs(n * n + a * n + b)):
        n += 1
    return n - 1

if __name__ == '__main__':
    ab_n = []
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            ab_n.append((get_max_prime(a, b), a, b))
    print max(ab_n)


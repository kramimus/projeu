#!/usr/bin/env python3

import itertools
import prime

def generate_permutations():
    for i in range(9, 0, -1):
        for p in itertools.permutations(range(i, 0, -1)):
            yield int(''.join((str(j) for j in p)))

if __name__ == '__main__':
    for p in generate_permutations():
        if prime.is_prime(p):
            print(p)
            break

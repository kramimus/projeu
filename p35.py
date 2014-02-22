#!/usr/bin/env python3

import prime

def generate_rotations(n):
    digits = [d for d in str(n)]
    rotations = set()
    for i in range(len(digits) - 1):
        digits = [digits[-1]] + digits[:-1]
        rotations.add(int(''.join(digits)))
    return rotations

if __name__ == '__main__':
    circular = []
    primes = prime.get_primes_up_to(int(1e6))
    while primes:
        p = primes.pop()
        rotations = generate_rotations(p)
        print(p, rotations)
        if primes & rotations == rotations:
            circular.append(p)
            circular += rotations
        primes -= rotations
    print(len(circular))

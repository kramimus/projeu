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

        # special case for 11
        if len(rotations) > 0 and next(iter(rotations)) == p:
            circular.append(p)

        elif primes & rotations == rotations:
            print(p, rotations)
            circular.append(p)
            circular += rotations
        primes -= rotations
    print(circular)
    print(len(circular))

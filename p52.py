#!/usr/bin/env python

import itertools

def check_for_permuted_multiples(n):
    multiples = [set(str(i*n)) for i in range(1, 7)]
    return all(i == multiples[0] for i in multiples)

if __name__ == "__main__":
    for n in itertools.count(start=1):
        if check_for_permuted_multiples(n):
            print([i*n for i in range(1, 7)])
            break


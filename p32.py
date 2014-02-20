#!/usr/bin/env python

import itertools
import string

ALL_DIGITS = '123456789'
digit_set = set(ALL_DIGITS)

found = set()
def check_soln(a, b, prod_digits):
    prod = a * b
    prod_set = set(str(prod))
    if len(prod_set) == len(str(prod)) and set(str(prod)) == set(prod_digits) and (a, b) not in found:
        print a, b, prod
        found.add((a, b))
        found.add((b, a))
        return prod
    else:
        return None


if __name__ == '__main__':
    solns = []
    terms_processed = set()
    for combo in itertools.combinations(ALL_DIGITS, 5):
        for perm in itertools.permutations(combo):
            remaining = digit_set - set(perm)
            for i in range(1, len(perm) - 1):
                a = int(''.join(perm[:i]))
                b = int(''.join(perm[i:]))
                prod = check_soln(a, b, remaining)
                if prod is not None:
                    solns.append(prod)
    print solns
    print sum(solns)

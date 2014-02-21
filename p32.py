#!/usr/bin/env python3

import itertools
import string

ALL_DIGITS = '123456789'
digit_set = set(ALL_DIGITS)

def check_soln(a, b, prod_digits):
    prod = a * b
    prod_set = set(str(prod))
    # no duplicating digits and uses the correct set
    if len(prod_set) == len(str(prod)) and set(str(prod)) == set(prod_digits):
        return prod
    else:
        return None


if __name__ == '__main__':
    solns = set()
    # empirically, it is only possible to use up all digits if we use
    # 5 digits in the multiplicands
    for combo in itertools.combinations(ALL_DIGITS, 5):
        for perm in itertools.permutations(combo):
            remaining = digit_set - set(perm)
            for i in range(1, len(perm) - 1):
                a = int(''.join(perm[:i]))
                b = int(''.join(perm[i:]))
                prod = check_soln(a, b, remaining)
                if prod is not None:
                    solns.add(prod)
    print(sum(solns))

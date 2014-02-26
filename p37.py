#!/usr/bin/env python3

import prime

def check_truncate_from_left(n, primes):
    digits = str(n)
    for i in range(1, len(digits)):
        if int(digits[i:]) not in primes:
            return False
    return True

def check_truncate_from_right(n, primes):
    digits = str(n)
    for i in range(1, len(digits)):
        if int(digits[:-i]) not in primes:
            return False
    return True



if __name__ == '__main__':
    # cheat and just assume we will see 11 in the 1st million
    primes = prime.get_primes_up_to(int(1e6))
    double_truncs = set()
    for p in primes:
        if check_truncate_from_left(p, primes) and check_truncate_from_right(p, primes):
            double_truncs.add(p)

    double_truncs -= set((2,3,5,7))
    print(double_truncs)
    print(sum(double_truncs))

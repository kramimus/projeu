#!/usr/bin/env python3

import itertools

def check_for_prime_divisible(n):
    divisors = [2,3,5,7,11,13,17]
    for divisor, subseq in zip(divisors, zip(*(n[i:] for i in range(1, 4)))):
        subnum = int(''.join(str(i) for i in subseq))
        if subnum % divisor != 0:
            return False
    return True

if __name__ == '__main__':
    pandig_weird_ones = []
    for n in itertools.permutations(range(10)):
        if check_for_prime_divisible(n):
            pandig_weird_ones.append(int(''.join(str(i) for i in n)))
    print(pandig_weird_ones)
    print(sum(pandig_weird_ones))

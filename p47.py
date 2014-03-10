#!/usr/bin/env python3

import factoring
import prime

def get_next_quad():
    prev_max = 0
    current_max = int(1e6)
    while True:
        primes = prime.get_primes_up_to(current_max)
        composites = [i for i in range(prev_max, current_max) if i not in primes]
        for i, comp in enumerate(composites):
            if composites[i+3] - comp == 3:
                yield comp

        prev_max = current_max
        current_max *= 10

def has_distinct_primes(start_of_4):
    for i in range(start_of_4, start_of_4 + 4):
        prime_factors = set(factoring.get_prime_factors(i))
        if len(prime_factors) < 4:
            return False
    return True

if __name__ == '__main__':
    for q in get_next_quad():
        if has_distinct_primes(q):
            for i in range(q, q + 4):
                print(i, factoring.get_prime_factors(i))
            break


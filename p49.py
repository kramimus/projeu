#!/usr/bin/env python3

import prime

def candidate_triplets():
    """ just solving the special case of 3330-separated primes
    """
    sieve = prime.get_primes_up_to(10000)
    for i in range(1000, 10000):
        if i in sieve and i + 3330 in sieve and i + 6660 in sieve:
            yield (i, i+3330, i+6660)
def all_permutations(triplet):
    return len(set(tuple(sorted(str(i))) for i in triplet)) == 1

if __name__ == '__main__':
    for trip in candidate_triplets():
        if all_permutations(trip) and trip[0] != 1487:
            print(''.join(str(i) for i in trip))

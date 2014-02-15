#!/usr/bin/env python

import factoring
import itertools

if __name__ == '__main__':
    abundant = factoring.get_abundant(range(2, 28124))
    pair_sums = {sum(pair) for pair in itertools.product(abundant, abundant)}
    non_paired = set(range(1, 28124)) - pair_sums

    print sum(non_paired)

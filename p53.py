#!/usr/bin/env python3

from functools import reduce
import math
from operator import mul

def n_combinations(n, r):
    return int(reduce(mul, range(r + 1, n + 1), 1) / math.factorial(n - r))

def get_counts(max_n):
    counts = []
    for n in range(1, max_n + 1):
        for r in range(1, n + 1):
            counts.append(n_combinations(n, r))
    return counts

if __name__ == '__main__':
    above_1e6 = [i for i in get_counts(100) if i > int(1e6)]
    print(len(above_1e6))

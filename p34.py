#!/usr/bin/env python3

import functools
import math

# only 10 factorials to worry about, precompute
factorials = tuple(math.factorial(i) for i in range(0, 10))

if __name__ == '__main__':

    sums = []
    for i in range(3, int(3e6)):
        s = sum(factorials[int(d)] for d in str(i))
        if s == i:
            sums.append(s)
    print(sum(sums))

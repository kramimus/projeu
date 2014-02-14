#!/usr/bin/env python

import factoring

def get_divisor_sums(nums):
    return {n: sum(factoring.get_proper_divisors(n)) for n in nums}

if __name__ == '__main__':
    divisor_sums = get_divisor_sums(range(1, 10000))
    amicable = []
    for i in range(2, 10000):
        sum_i = divisor_sums[i]
        if i == divisor_sums.get(sum_i, 0) and sum_i != i:
            print i, sum_i
            amicable.append(i)

    print sum(amicable)

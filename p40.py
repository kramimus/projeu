#!/usr/bin/env python3

from functools import reduce
import math
from operator import mul

def remove_full_ranges(digit_n):
    digit_n -= 10
    start = 10
    exp = 2
    current_max = int(10**exp)
    while digit_n > current_max * exp:
        print(digit_n, current_max * exp)
        digit_n -= (current_max - start) * exp
        start += int(10**exp)
        exp += 1
        current_max = int(10**exp)
    return exp, digit_n, start

def easy_way(max_target):
    digit_count = math.log(max_target, 10)
    concated = ''
    print(int(max_target // digit_count))
    for i in range(1, int(max_target // (digit_count - 1))):
        concated += str(i)
    return concated

if __name__ == '__main__':
    targets = [1, 10, 100, 1000, 10000, 100000, 1000000]
    # digits = []
    # for target in targets:
    #     if target < 10:
    #         digits.append(target)
    #         continue
    #     print(target)
    #     digit_count, remainder, start = remove_full_ranges(target)
    #     number = start + remainder // digit_count
    #     place = remainder % digit_count
    #     print(digit_count, remainder, number, place)
    #     digits.append(int(str(number)[place]))
    #     print(digits)

    prod = 1
    frac_string = easy_way(targets[-1])
    for target in targets:
        prod *= int(frac_string[target-1])
    print(prod)

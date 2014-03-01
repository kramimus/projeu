#!/usr/bin/env python3

from collections import Counter
import math

def check_integer_sides(a, b, perimeter):
    """ check if c is integral

    avoid using sqrt for both speed and round-off issues
    """
    c_sq = a*a + b*b
    perimeter_c = perimeter - a - b
    return c_sq == perimeter_c * perimeter_c

def count_integral_rights(p):
    sides = set()
    # a+b must be greater than p/2 and less than approx p*0.6
    for a in range(1, math.ceil(p * 0.6)):
        for b in range(max(a, math.floor((p* 0.5) - a)), math.ceil((p * 0.6) - a)):
            if check_integer_sides(a, b, p):
                sides.add((a, b))
    return len(sides)

if __name__ == '__main__':
    c = Counter()
    for i in range(1, 1001):
        c[i] = count_integral_rights(i)
    print(c.most_common(5))

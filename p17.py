#!/usr/bin/env python

NUM_COUNTS = (
    (90, 6),
    (80, 6),
    (70, 7),
    (60, 5),
    (50, 5),
    (40, 5),
    (30, 6),
    (20, 6),
    (19, 8),
    (18, 8),
    (17, 9),
    (16, 7),
    (15, 7),
    (14, 8),
    (13, 8),
    (12, 6),
    (11, 6),
    (10, 3),
    (9, 4),
    (8, 5),
    (7, 5),
    (6, 3),
    (5, 4),
    (4, 4),
    (3, 5),
    (2, 3),
    (1, 3))

def digit_count(n):
    for div, count in NUM_COUNTS:
        if n / div > 0:
            return count, n % div
    return 0, n

def count_letters(n, has_hundreds):
    and_modifier = 3 if has_hundreds else 0
    count, rest = digit_count(n)
    if n == 1000:
        return 11
    elif n >= 100:
        hundreds = n / 100
        return count_letters(n % 100, True) + digit_count(hundreds)[0] + 7
    elif n > 19:
        return count_letters(rest, False) + count + and_modifier
    elif n > 0:
        return count + and_modifier
    return 0

if __name__ == '__main__':
    print sum(count_letters(i, 0) for i in range(1001))

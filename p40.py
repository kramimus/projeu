#!/usr/bin/env python3

def remove_full_ranges(digit_n):
    if digit_n < 10:
        return 1, digit_n
    else:
        digit_n -= 9

    exp = 2
    current_max = int(10**exp) - 1
    while digit_n > current_max * exp:
        digit_n -= current_max * exp
        exp += 1
        current_max = int(10**exp) - 1
    return exp, digit_n

if __name__ == '__main__':
    targets = [1, 10, 100, 1000, 10000, 100000, 1000000]
    digits = []
    for target in targets:
        digit_count, remainder = remove_full_ranges(target)
        print(digit_count, remainder)
        number = remainder // digit_count
        place = remainder % digit_count
        digits.append(int(str(number)[place]))
        print(digits)

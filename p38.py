#!/usr/bin/env python3

if __name__ == '__main__':
    maxes = []
    for i in range(int(1e6)):
        prev = 0
        n = 1
        total = str(i)
        while len(total) < 10:
            prev = total
            n += 1
            total += str(n * i)
        digits = set(prev)
        digits.discard('0')
        if len(digits) == 9:
            maxes.append((int(prev), n - 1, i, len(prev)))
    print(max(maxes))

#!/usr/bin/env python

if __name__ == '__main__':
    digit_summers = []
    for i in range(2, 999999):
        digit_sum = sum(int(j)**5 for j in str(i))
        if digit_sum == i:
            digit_summers.append(i)
    print digit_summers
    print sum(digit_summers)

#!/usr/bin/env python3

if __name__ == '__main__':
    digit_summers = []
    # just brute force this one, we can't make numbers bigger than 1e6 with n**5
    for i in range(2, 999999):
        digit_sum = sum(int(j)**5 for j in str(i))
        if digit_sum == i:
            digit_summers.append(i)
    print(sum(digit_summers))

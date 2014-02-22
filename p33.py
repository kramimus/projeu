#!/usr/bin/env python3

def check_frac(num, denom):
    if num % 10 == 0 and denom % 10 == 0:
        return False

    num_digits = [int(i) for i in str(num)]
    denom_digits = [int(i) for i in str(denom)]
    matching_digits = set(num_digits) & set(denom_digits)
    if not matching_digits:
        return False
    reduced_denom = float(denom) / num
    for d in matching_digits:
        non_cancelled_num = num_digits[0] if num_digits[1] == d else num_digits[1]
        non_cancelled_denom = denom_digits[0] if denom_digits[1] == d else denom_digits[1]
        if non_cancelled_num * reduced_denom == non_cancelled_denom:
            return True

if __name__ == '__main__':
    fracs = []
    for i in range(11, 99):
        for j in range(11, 99):
            if i < j and check_frac(i, j):
                print(i, j)
                fracs.append((i, j))
    num = 1
    denom = 1
    for i, j in fracs:
        num *= i
        denom *= j
    if denom % num == 0:
        print(denom // num)

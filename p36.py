#!/usr/bin/env python3

if __name__ == '__main__':
    double_palin = []
    for i in range(1, int(1e6)):
        base10_digits = list(str(i))
        base2_digits = list(bin(i)[2:])

        if base2_digits[-1] != '0' and \
          base10_digits == list(reversed(base10_digits)) and \
          base2_digits == list(reversed(base2_digits)):
            double_palin.append(i)
    print(sum(double_palin))

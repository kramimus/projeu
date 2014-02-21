#!/usr/bin/env python3

remaining_power = {}

if __name__ == '__main__':
    terms = set()
    for a in range(2, 101):
        for b in range(2, 101):
            # filter out products that have already been computed at lower a
            if a not in remaining_power or b > remaining_power[a]:
                prod = a**b
                remaining_power[prod] = 100 // b
                terms.add(prod)
    print(len(terms))

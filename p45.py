#!/usr/bin/env python3

import itertools

def get_pentagonal(start, end):
    return set(int(i * (3 * i - 1) // 2) for i in range(start, end + 1))

def get_hexagonal(start, end):
    return set(int(i * (2 * i - 1)) for i in range(start, end + 1))

def next_triangle(tri_start):
    for i in itertools.count(start=tri_start):
        yield i, int(i * (i + 1) // 2)

def get_tri_pent_hex_match(tri_start):
    pents = set()
    hexs = set()
    last_pent = 0
    last_hex = 0
    for i, tri in next_triangle(tri_start):
        max_pent = int(i * 1.8)
        max_hex = i * 2
        if last_pent < max_pent:
            pents |= get_pentagonal(last_pent + 1, max_pent)
            last_pent = max_pent
        if last_hex < max_hex:
            hexs |= get_hexagonal(last_hex + 1, max_hex)
            last_hex = max_hex
        if tri in pents and tri in hexs:
            return i, tri

if __name__ == '__main__':
    print(get_tri_pent_hex_match(286))

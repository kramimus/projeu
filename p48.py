#!/usr/bin/env python3

if __name__ == '__main__':
    # sadly, python's arbitrary precision arithmetic makes this too easy
    print(sum(i**i for i in range(1, 1001)))

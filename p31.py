#!/usr/bin/env python

import itertools

COIN_VALS = [1, 2, 5, 10, 20, 50, 100, 200]
COIN_MAXES = [(200 / i) for i in COIN_VALS]

def add_coins(coin_tuple):
    return sum(a * b for a, b in zip(coin_tuple, COIN_VALS))

def brute_force():
    ranges = [range(0, coin_max + 1) for coin_max in COIN_MAXES]
    print sum(int(add_coins(coin_counts) == 200) for coin_counts in itertools.product(*ranges))

memoized = {}
def get_combinations(coins_left, total):
    key = (tuple(coins_left), total)
    if key in memoized:
        return memoized[key]
    if not coins_left:
        return 1 if total == 0 else 0

    curr_coin = coins_left[-1]
    combos = 0
    for i in range(0, (total / curr_coin) + 1):
        combos += get_combinations(coins_left[:-1], total - (i * curr_coin))
    memoized[key] = combos
    return combos

if __name__ == '__main__':
    print get_combinations(COIN_VALS, 200)

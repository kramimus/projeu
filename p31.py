#!/usr/bin/env python3

import functools
import itertools

COIN_VALS = (1, 2, 5, 10, 20, 50, 100, 200)

#memoize
@functools.lru_cache(maxsize=None)
def get_combinations(coins_left, total):
    """ for each call go through possible counts of a coin

    recursively build combos of remaining coins with remaining value
    """
    if not coins_left:
        return 1 if total == 0 else 0

    curr_coin = coins_left[-1]
    combos = 0
    for i in range(0, (total // curr_coin) + 1):
        combos += get_combinations(tuple(coins_left[:-1]), total - (i * curr_coin))
    return combos

if __name__ == '__main__':
    print(get_combinations(COIN_VALS, 200))

#!/usr/bin/env python3

import itertools
import sys

def get_pentagonal(i):
    return int(i*(3*i - 1) // 2)

def next_pentagonal():
    candidate_idx = 1
    # lookahead f __index for checking the p_j + p_k sums, doing some
    # math, you can see that you only need to go about a factor of
    # sqrt(2) in n
    gen_ahead_idx = int(candidate_idx * 1.5)
    tri_so_far = set()
    j = 1
    while True:
        while j < gen_ahead_idx:
            tri_so_far.add(get_pentagonal(j))
            j += 1

        candidate = get_pentagonal(candidate_idx)
        for lesser_tri in tri_so_far:
            if candidate - lesser_tri in tri_so_far and candidate + lesser_tri in tri_so_far:
                yield (lesser_tri, candidate)
        candidate_idx += 1
        gen_ahead_idx = int(candidate_idx * 1.5)


# this is a hack, this only prints diffs infinitely and the user is
# supposed to stop it when they think it is done
#
# empirically, the first (smallest k,j) pentagonal pair is the one you want
if __name__ == '__main__':
    min_diff  = None
    for (smaller, bigger) in next_pentagonal_pair():
        diff = bigger - smaller
        if min_diff is None or diff < min_diff:
            min_diff = diff
            print(min_diff)

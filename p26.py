#!/usr/bin/env python

def get_cycle_length(divisor):
    """ long division looking for first repeated divisor/modulus pair
    """
    div_mods = list()
    div = 0
    mod = 1
    while mod > 0 and (div, mod) not in div_mods:
        div_mods.append((div, mod))
        mod *= 10
        div = mod / divisor
        mod %= divisor

    if mod > 0:
        return len(div_mods) - div_mods.index((div, mod))
    else:
        return 0

if __name__ == '__main__':
    lengths = [(get_cycle_length(i), i) for i in range(2, 1000)]
    print max(lengths)


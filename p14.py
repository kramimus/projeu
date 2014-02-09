#!/usr/bin/env python

# memoize
seq_dict = {}

def next_seq(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def seq_length(n):
    if n == 1:
        return 1
    elif n in seq_dict:
        return seq_dict[n]
    else:
        return 1 + seq_length(next_seq(n))

if __name__ == '__main__':
    max_seq = 0
    max_start = -1
    for i in range(1, int(1e6)):
        l = seq_length(i)
        print i, l
        seq_dict[i] = l
        if l > max_seq:
            max_seq = l
            max_start = i
    print max_start, max_seq

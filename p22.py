#!/usr/bin/env python

import string
import sys

def letter_score(word):
    print word
    return sum(string.lowercase.index(i) + 1 for i in word)

if __name__ == '__main__':
    fname = sys.argv[1]
    lines = (l.lower().strip() for l in open(fname) if l)
    quoted_names = sum((l.split(',') for l in lines), [])
    names = [n.replace('"', '') for n in quoted_names]
    names.sort()
    score = 0
    for i, name in enumerate(names, 1):
        score += i * letter_score(name)
    print score

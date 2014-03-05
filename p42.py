#!/usr/bin/env python3

import csv
import itertools
import string

def get_words(fword):
    words = []
    with open(fword) as f:
        reader = csv.reader(f)
        for row in reader:
            words += row
    return words

def get_max_triangle_value(words):
    return max(len(n) for n in words) * 26

def get_triangle_numbers_up_to(max_tri):
    tri_nums = set()
    curr_tri = 0
    for i in itertools.count(start=1):
        curr_tri = 0.5 * i * (i + 1)
        tri_nums.add(curr_tri)
    return tri_nums

def words_to_nums(words):
    word_nums = {}
    for word in words:
        word_nums[word] = sum(string.ascii_uppercase.index(c) + 1 for c in word)
    return word_nums

if __name__ == '__main__':
    words = get_words('words.txt')
    nums = get_triangle_numbers_up_to(get_max_triangle_value(words))
    word_nums = words_to_nums(words)
    tri_words = [word for word, s in word_nums.items() if s in nums]
    print(tri_words)
    print(len(tri_words))

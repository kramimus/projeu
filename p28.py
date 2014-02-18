#!/usr/bin/env python

if __name__ == '__main__':
    curr_sum = 1
    prev_max = 1
    for i in range(3, 1002, 2):
        ring_max = i * i
        ring_min = prev_max + 1
        ne = ring_max
        sw = (ring_max - ring_min) / 2 + ring_min
        se = (sw - ring_min) / 2 + ring_min
        nw = (ring_max - sw) / 2 + sw
        curr_sum += ne + nw + sw + se
        prev_max = ring_max
    print curr_sum

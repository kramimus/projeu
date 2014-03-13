#!/usr/bin/env python3

from collections import Counter
import prime

def make_n2_sum(n):
    sum_lengths = Counter()
    prime_set = prime.get_primes_up_to(n)
    sorted_primes = sorted(prime_set)

    sums = [0]
    current_sum = 0
    for p in sorted_primes:
        current_sum += p
        sums.append(current_sum)

    max_length = 0
    for p in sorted_primes:
        for length, prime_sum in enumerate(sums):
            if max_length < length and prime_sum in prime_set:
                    max_length = length
                    sum_lengths[prime_sum] = max(sum_lengths[prime_sum], length)
        sums = [i - p for i in sums[1:]]
        if len(sums) < max_length:
            break
    return sum_lengths

if __name__ == '__main__':
    sum_lengths = make_n2_sum(int(1e6))
    print(sum_lengths.most_common(1))

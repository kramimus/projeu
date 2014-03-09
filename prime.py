from collections import OrderedDict
import math

prime_cache = {}

def is_prime(n):
    if n in prime_cache:
        return prime_cache[n]

    prime = True
    for i in range(2, min(n, int(math.sqrt(n)) + 1)):
        if n % i == 0:
            prime = False
            break
    prime_cache[n] = prime
    return prime


def get_primes_up_to(max_n):
    """ sieve of erasthenes
    """
    limit = max_n + 1
    primes = set()
    numbers_left = [True] * limit
    numbers_left[0] = numbers_left[1] = False

    for i, isprime in enumerate(numbers_left):
        if isprime:
            primes.add(i)
            for n in range(i*i, limit, i):
                numbers_left[n] = False
    return primes

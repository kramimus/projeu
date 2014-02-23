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
    primes = set()
    numbers_left = OrderedDict((i, True) for i in range(2, max_n))
    while numbers_left:
        new_prime = numbers_left.popitem(last=False)[0]
        primes.add(new_prime)
        for i in range(new_prime*2, max_n, new_prime):
            try:
                del numbers_left[i]
            except KeyError:
                pass
    return primes

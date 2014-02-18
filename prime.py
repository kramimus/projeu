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



import math

def get_prime_factors(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return [i] + get_prime_factors(n / i)
    else:
        return [n]
    return factors

def get_proper_divisors(n, j=2):
    return [i for i in range(1, n) if n % i == 0]

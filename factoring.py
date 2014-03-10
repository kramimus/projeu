import math

def get_prime_factors(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return [i] + get_prime_factors(n / i)
    else:
        return [int(n)]
    return []

def get_proper_divisors(n, j=2):
    return [i for i in range(1, n) if n % i == 0]

def get_divisor_sums(nums):
    return {n: sum(get_proper_divisors(n)) for n in nums}

def get_amicable(nums):
    divisor_sums = get_divisor_sums(nums)
    amicable = []
    for i in nums:
        sum_i = divisor_sums[i]
        if i == divisor_sums.get(sum_i, 0) and sum_i != i:
            amicable.append(i)

def get_abundant(nums):
    divisor_sums = get_divisor_sums(nums)
    return [i for i in nums if i < divisor_sums[i]]

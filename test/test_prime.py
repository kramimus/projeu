import prime
import unittest

class SieveTest(unittest.TestCase):

    sample_primes = set((2, 3, 5, 7, 11, 13, 7919))

    def test_sieve_some_primes(self):
        sieve = prime.get_primes_up_to(max(self.sample_primes))
        self.assertFalse(self.sample_primes - sieve)

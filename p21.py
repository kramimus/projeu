#!/usr/bin/env python

import factoring


if __name__ == '__main__':
    amicable = factoring.get_amicable(range(2, 10000))
    print sum(amicable)

#!/usr/bin/env python3

import sys
from math import sqrt

def is_prime(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2 ):
        if n % i == 0:
            return False
    return True

def get_prime(prime_index):
    num = 0
    prime_count = 0
    while prime_count < prime_index:
        num += 1
        if is_prime(num) == True:
            prime_count += 1
    return(num)


if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        print(get_prime(int(sys.argv[i])))

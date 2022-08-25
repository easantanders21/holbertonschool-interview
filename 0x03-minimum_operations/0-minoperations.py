#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Minimum Operations """
    if type(n) is not int or n <= 1:
        return 0

    factors = 0
    count = 2

    while count <= n:
        if n % count != 0:
            count += 1
        else:
            factors += count
            n /= count
    return factors

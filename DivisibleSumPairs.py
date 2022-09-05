#!/bin/python3

import math
import os
import random
import re
import sys

#
# Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i<j and  ar[i] + ar[j]
# is divisible by k.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    subarrays = list()
    i = 0
    while i < n:
        for j in ar[i + 1:]:
            if (ar[i] + j) % k == 0:
                subarrays.append([ar[i], j])
        i += 1
    return len(subarrays)

if __name__ == '__main__':
    n = 6
    k = 3

    ar = [1, 3, 2, 6, 1, 2]

    result = divisibleSumPairs(n, k, ar)

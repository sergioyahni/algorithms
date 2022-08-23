#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    print(f"n = {n}\nk = {k}\nar = {ar}")

    subarrays = list()
    i = 0
    while i < n:
        for j in ar[i + 1:]:
            if (ar[i] + j) % k == 0:
                subarrays.append([ar[i], j])
        i += 1
    return len(subarrays)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

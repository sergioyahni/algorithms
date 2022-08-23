#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    subarrays = []
    n = 0
    status = True
    while status:
        if n + m > len(s):
            status = False
        else:
            if sum(s[n:n+m]) == d:
                subarrays.append(s[n:n+m])
        n += 1
    return len(subarrays)

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(result)
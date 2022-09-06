#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
# Given an array of integers, find the longest subarray where the absolute difference between any two elements is
# less than or equal to 1.

# The function should Returns the length of the longest subarray that meets the criterion


# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    subs, sub, n, large = list(), list(), 0, 0

    while n <= len(a) - 1:
        if abs(a[0] - a[n]) <= 1:
            sub.append(a[n])
        else:
            subs.append(sub)
            a[0] = a[n]
            sub = [a[0]]
        n += 1
    if subs == []:
        subs.append(sub)
    for item in subs:
        large = len(item) if len(item) > large else large
    return large


if __name__ == '__main__':
    # a = [4, 6, 5, 3, 3, 1]  # 3
    # a = [1, 2, 2, 3, 1, 2] # 5
    a = [66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
         66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
         66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
         66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66]
    print(len(a))
    result = pickingNumbers(a)
    print("result:", result)

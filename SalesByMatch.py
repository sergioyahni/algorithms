#!/bin/python3

import math
import os
import random
import re
import sys

#
# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of
# each sock, determine how many pairs of socks with matching colors there are.
#
# Complete the sockMerchant function in the editor below.
#
# sockMerchant has the following parameter(s):
#
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    print(f"n={n}\tar={ar}")
    pairs = 0
    mid_set = set(ar)
    for element in mid_set:
        pairs += int(ar.count(element) / 2)
    return pairs

if __name__ == '__main__':
    n = 9

    # ar = list(map(int, input().rstrip().split()))
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20, 40, 20]

    result = sockMerchant(n, ar)

    print(result)
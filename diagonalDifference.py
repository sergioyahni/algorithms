#!/bin/python3

import math
import os
import random
import re
import sys

# Given a square matrix, calculate the absolute difference
# between the sums of its diagonals.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


def diagonalDifference(arr):
    # Write your code here
    n, m = 0, len(arr) - 1
    ltr, rtl = 0, 0
    while n < len(arr):
        ltr += arr[n][n]
        rtl += arr[n][m]
        n += 1
        m -= 1
    return abs(ltr - rtl)


if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonalDifference(arr)
    print(result)

    """
    11 2 4
    4 5 6
    10 8 -12
    """
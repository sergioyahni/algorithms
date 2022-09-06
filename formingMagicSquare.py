#!/bin/python3

import math
import os
import random
import re
import sys

#
# We define a magic square to be an n*n matrix of distinct positive integers from 1 to n^2  where the sum of any row,
# column, # or diagonal of length  is always equal to the same number: the magic constant.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

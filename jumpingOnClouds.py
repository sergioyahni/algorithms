#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    pos = 0
    steps = 0
    calculate = True

    indices = [i for i, x in enumerate(c) if x == 1]

    while calculate:
        if pos + 2 <= len(c) and pos + 2 not in indices:
            pos += 2
            steps += 1
        elif pos + 1 < len(c):
            pos += 1
            steps += 1
        else:
            calculate = False

    return steps


if __name__ == '__main__':
    n = 7

    c = [0, 0, 1, 0, 0, 1, 0]

    result = jumpingOnClouds(c)
    print(result)

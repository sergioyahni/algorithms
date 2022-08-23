#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    q1 = q.copy()
    q1.sort()

    for item in q1:
        result = q1.index(item) - q.index(item)
        if result > 2:
            return "Too chaotic"
        if result > 0:
            bribes += result

    print(q1)
    print(q)
    return bribes + 1


if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    print(minimumBribes(q))

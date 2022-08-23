#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    bird_type = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
    for i in arr:
        bird_type[str(i)] += 1

    v = list(bird_type.values())
    k = list(bird_type.keys())
    return k[v.index(max(v))]


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)
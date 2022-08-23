#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    chigh = [scores[0]]
    clow = [scores[0]]

    for score in scores:
        if score > chigh[-1]:
            chigh.append(score)
        elif score < clow[-1]:
            clow.append(score)

    return len(chigh) - 1, len(clow) - 1


if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
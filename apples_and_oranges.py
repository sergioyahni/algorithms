#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples_counter = 0
    for apple in apples:
        if s <= a + apple <= t:
            apples_counter += 1
    print(apples_counter)

    oranges_counter = 0
    for orange in oranges:
        if s <= b + orange <= t:
            oranges_counter =+ 1
    print(oranges_counter)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    print(first_multiple_input)
    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    print(second_multiple_input)

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    print(third_multiple_input)
    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    print(apples)

    oranges = list(map(int, input().rstrip().split()))
    print(oranges)

    countApplesAndOranges(s, t, a, b, apples, oranges)

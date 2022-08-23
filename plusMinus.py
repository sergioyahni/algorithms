#!/bin/python3

import math
import os
import random
import re
import sys

#
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos, zero, neg = 0, 0, 0
    for item in arr:
        if item > 0:
            pos += 1
        elif item < 0:
            neg += 1
        else:
            zero += 1
    print("{0:.6f}".format(pos/ len(arr)))
    print("{0:.6f}".format(neg/ len(arr)))
    print("{0:.6f}".format(zero/ len(arr)))


if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]

    print(plusMinus(arr))

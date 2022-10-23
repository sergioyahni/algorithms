#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'utopianTree' function below: The Utopian Tree goes through 2 cycles of growth every year. Each
# spring, it doubles in height. Each summer, its height increases by 1 meter.
#
# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n
# growth cycles?
#
# The function is expected to return an INTEGER. The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    cycle, m = 1, 1
    if n == 0:
        return cycle

    else:
        while m <= n:
            cycle = cycle * 2 if m % 2 != 0 else cycle + 1
            m += 1
    return cycle


if __name__ == '__main__':
    t = [0, 1, 4]
    # n = 2
    # print(utopianTree(n))

    for n in t:
        print(utopianTree(n))

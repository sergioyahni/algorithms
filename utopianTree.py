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
# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after
# n growth cycles? The function is expected to return an INTEGER. The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    tree = 0
    for cycle in range(0, n):
        # print('c', cycle)
        if cycle == 0:
            tree = 1
        else:
            if cycle % 2 != 0:
                tree += tree
            else:
                tree += 1

    return tree


if __name__ == '__main__':

    n = [0, 1, 4]
    for t_itr in n:
        print(utopianTree(t_itr))


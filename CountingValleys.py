#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    valley = 0
    move = 0

    for step in path:
        print(step)
        if step == "D":
            move += -1
            if move < 0 and valley == 0:
                valley = 1

        elif step == "U":
            move += 1
            if move >= 0 and valley == 1:
                valleys += 1
                valley = 0
        print(move)
    return valleys


if __name__ == '__main__':
    steps = 8
    path = "UDDDUDUU"
    result = countingValleys(steps, path)
    print('valleys:', result)

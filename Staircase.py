#!/bin/python3

import math
import os
import random
import re
import sys


# In the 'staircase' function below the base and height are both equal to n.
# It is drawn using # symbols and spaces.
# The last line is not preceded by any spaces.
#
# The function accepts INTEGER n as parameter.


def staircase(n):
    # Write your code here
    x = 1
    while x <= n:
        print(' ' * (n - x) + '#' * x)
        x += 1


if __name__ == '__main__':
    n = 6
    staircase(n)

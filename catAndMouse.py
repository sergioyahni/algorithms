#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
# Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to
# determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed.
# If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.


def catAndMouse(x, y, z):
    A = abs(x - z)
    B = abs(y - z)
    if A == B:
        return 'Mouse C'
    elif A > B:
        return 'Cat B'
    else:
        return 'Cat A'


if __name__ == '__main__':
    x = 1
    y = 3
    z = 2

    result = catAndMouse(x, y, z)
    print(result)

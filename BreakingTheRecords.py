#!/bin/python3

import math
import os
import random
import re
import sys

#
# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates
# the number of times she breaks her season record for most points and least points in a game. Points scored in the
# first game establish her record for the season, and she begins counting from there.
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
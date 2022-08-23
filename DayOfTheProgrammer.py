#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year < 1918 and year % 4 == 0:
        return f"{30 - (274 - 256)}.09.{year}"

    elif year == 1918:
        return "26.09.1918"
    elif (year > 1918) and year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return f"{30 - (274 - 256)}.09.{year}"
    else:
        return f"{30 - (273 - 256)}.09.{year}"


if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)

#!/bin/python3

import math
import os
import random
import re
import sys

# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for
# each year of their total age. They will only be able to blow out the tallest of the candles.
# Count how many candles are tallest.
#
# Example:
#
# candles = [4, 4, 1, 3]
# The maximum height candles are 4 units high. There are 2 of them, so return 2.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here

    numerator = 0
    for candle in candles:
        numerator += 1 if candle == max(candles) else 0

    return numerator


if __name__ == '__main__':
    candles = [5, 3, 2, 5, 1, 3, 4, 5]
    result = birthdayCakeCandles(candles)
    print(result)
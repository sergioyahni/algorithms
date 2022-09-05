#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split.
# Otherwise, it should print the integer amount of money that Brian owes Anna.
#
# bonAppetit has the following parameter(s):
#
# bill: an array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money that Anna contributed to the bill
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    calculate_bill = int(b - (sum(bill) - bill[k]) / 2)
    if calculate_bill == 0:
        print("Bon Appetit")
    else:
        print(calculate_bill)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

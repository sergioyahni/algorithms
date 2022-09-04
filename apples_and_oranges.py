#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'countApplesAndOranges' function below. Sam's house has an apple tree and an orange tree that yield an
# abundance of fruit. Using the information given below, determine the number of apples and oranges that land on
# Sam's house.
#
# In the diagram below: * The red region denotes the house, where s is the start point, and t is the endpoint. The
# apple tree is to the left of the house, and the orange tree is to its right.
#
# * Assume the trees are located on a # single point, where the apple tree is at point a , and the orange tree is at
# point b.
#
# * When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis.
#
# * A negative value of  means the fruit fell units to the tree's left, and a positive value of  means it falls  units
# to the tree's right.
#
# The function accepts following parameters: 1. INTEGER s 2. INTEGER t 3. INTEGER a 4. INTEGER b 5. INTEGER_ARRAY
# apples 6. INTEGER_ARRAY oranges
#
# https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples_counter = [1 if s <= a + apple <= t else 0 for apple in apples]
    print(sum(apples_counter))

    oranges_counter = [1 if t >= (b + orange) >= s else 0 for orange in oranges]
    print(sum(oranges_counter))


if __name__ == '__main__':
    s = 7
    t = 11
    a = 5
    b = 15

    apples = [-2, 2, 1]
    oranges = [5, -6]

    countApplesAndOranges(s, t, a, b, apples, oranges)

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # create a list of possible combinations
    def n_length_combo(lst=arr, n=4):

        if n == 0:
            return [[]]

        l = []
        for i in range(0, len(lst)):

            m = lst[i]
            remLst = lst[i + 1:]

            remainlst_combo = n_length_combo(remLst, n - 1)
            for p in remainlst_combo:
                l.append([m, *p])
        return l
    combo = n_length_combo()
    minimum, maximum = sum(combo[0]), 0
    for item in combo:
        x = sum(item)
        maximum = x if maximum < x else maximum
        minimum = x if minimum > x else minimum

    print(minimum, maximum)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
#!/bin/python3

import math
import os
import random
import re
import sys


#
# A teacher asks the class to open their books to a page number. A student can either start turning pages from the
# front of the book or from the back of the book. They always turn pages one at a time. When they open the book,
# page 1 is always on the right side:
# When they flip page 1, they see pages 2 and 3. Each page except the last page will always be printed on both sides.
# The last page may only be printed on the front, given the length of the book. If the book is n pages long, and a
# student wants to turn to page p, what is the minimum number of pages to turn? They can start at the beginning or the
# end of the book.
#
# Given  and , find and print the minimum number of pages that must be turned in order to arrive at page .
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here

    res_ftl, res_ltf = int(), int()

    pcounter, pl, pr = 0, 0, 1
    c = False

    while not c and pl < n:
        if pl == p or pr == p:
            res_ftl = pcounter
            c = True
        else:
            pcounter += 1
            pl += 2
            pr += 2

    pcounter1 = 0

    if n % 2 == 0:
        pl1, pr1 = n, n + 1
    else:
        pl1, pr1 = n - 1, n

    c1 = False
    while not c1 and pl > 0:

        if pl1 == p or pr1 == p:
            res_ltf = pcounter1
            c1 = True
        else:
            pl1 -= 2
            pr1 -= 2
        pcounter1 += 1

    # print(res_ftl, res_ltf)
    if res_ftl > res_ltf:
        return res_ltf
    else:
        return res_ftl


if __name__ == '__main__':
    n = 6
    p = 5

    # n = 5
    # p = 4

    result = pageCount(n, p)

    print(result)

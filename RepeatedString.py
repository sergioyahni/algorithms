#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    sherit = n % len(s)
    a_in_sherit = s[:sherit].count('a')
    num = n // len(s)
    a_in_main_body = s.count('a') * num


    return a_in_main_body + a_in_sherit

if __name__ == '__main__':

    s = 'aadcdaccacabdaabadadaabacdcbcacabbbadbdadacbdadaccbbadbdcadbdcacacbcacddbcbbbaaccbaddcabaacbcaabbaaa'
    # s = "aba"

    # n = 10
    n = 942885108885

    result = repeatedString(s, n)

    print(result)

    # result = 330009788107
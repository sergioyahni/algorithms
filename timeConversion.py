#!/bin/python3

import math
import os
import random
import re
import sys


# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def timeConversion(s):
    # Write your code here

    if s[-2:] == 'PM' and s[:2] != str(12):
        nt = f"{int(s[:2]) + 12}:{s[3:8]}"
    elif s[-2:] == 'PM' and s[:2] == str(12):
        nt = f"12:{s[3:8]}"
    elif s[-2:] == 'AM' and s[:2] != str(12):
        nt = s[:-2]
    elif s[-2:] == 'AM' and s[:2] == str(12):
        nt = f'00:{s[3:8]}'
    else:
        return False
    return nt


if __name__ == '__main__':
    s = '12:40:25AM'

    result = timeConversion(s)
    print(result)

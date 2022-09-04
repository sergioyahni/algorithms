#!/bin/python3

import math
import os
import random
import re
import sys


#
# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:
#
# If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    ngl = list()
    for grade in grades:
        if grade < 38:
            ngl.append(grade)
        else:
            dif = grade % 5
            g = 5 - dif
            ng = grade if g > 2 else grade + g
            ngl.append(ng)

    return ngl


if __name__ == '__main__':
    grades = [73, 67, 38, 33]
    print(gradingStudents(grades))

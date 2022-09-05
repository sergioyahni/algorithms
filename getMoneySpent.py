#!/bin/python3

import os
import sys


#
# A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give
# budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not
# possible to buy both items, return -1.
#

def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    max_price = -1
    keyboards.reverse()
    drives.reverse()
    for keyboard in keyboards:
        for drive in drives:
            max_price = keyboard + drive if max_price < keyboard + drive <= b else max_price
    return max_price


if __name__ == '__main__':
    b = 60
    keyboards = [40, 50, 60]
    drives = [5, 8, 12]

    # b = 10
    # keyboards = [3, 1]
    # drives = [5, 2, 8]

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)

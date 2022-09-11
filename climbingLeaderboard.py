#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'climbingLeaderboard' function below. An arcade game player wants to climb to the top of the
# leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:
#
# The player with the highest score is ranked number 1 on the leaderboard. Players who have equal scores receive the
# same ranking number, and the next player(s) receive the immediately following ranking number.
#
# The function is
# expected to return an INTEGER_ARRAY.
#
# The function accepts following parameters: 1. INTEGER_ARRAY ranked 2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    rank = []
    for game in player:
        rank.append(sorted(list(set(ranked[:] + [game])), reverse=True).index(game) + 1)
    return rank

    # rank = [sorted(list(set(ranked[:] + [game])), reverse=True).index(game) + 1) for game in player]


if __name__ == '__main__':
    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [5, 25, 50, 120]

    result = climbingLeaderboard(ranked, player)
    print(result)

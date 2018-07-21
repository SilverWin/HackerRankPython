#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/itertools-combinations/problem"""

__author__ = "Filip Jankowski"

from itertools import combinations

inpt = input().split(" ")
combinations_list = []
for i in range(int(inpt[1])):
    combinations_list.extend(list(combinations(sorted(inpt[0]), i+1)))
for x in combinations_list:
    print("".join(x))
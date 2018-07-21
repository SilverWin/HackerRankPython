#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/itertools-permutations/problem"""

__author__ = "Filip Jankowski"

from itertools import permutations

inpt = input().split(" ")
permutationslist = list(permutations(inpt[0], int(inpt[1])))
permutationslist.sort()
for i in permutationslist:
    print("".join(i))
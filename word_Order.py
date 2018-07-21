#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/word-order/problem"""

__author__ = "Filip Jankowski"

from collections import OrderedDict

n = int(input())
wordsdict = OrderedDict()
nodw = 0
noo = []
for x in range(n):
    s = input()
    if s in wordsdict:
        wordsdict[s] += 1
    else:
        wordsdict[s] = 1
for i in wordsdict:
    nodw += 1
    noo.append(str(wordsdict[i]))
print(str(nodw))
print(" ".join(noo))
#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/iterables-and-iterators/problem"""

__author__ = "Filip Jankowski"

from itertools import combinations

n = int(input())
s = input().split(" ")
k = int(input())
l = 0

indcs = tuple(combinations([x for x in range(1, n+1)], k))

indx = [x + 1 for x in range(n) if s[x] == 'a']

for i in indcs:
    if set(indx).intersection(set(i)).__len__() != 0:
        l += 1

print(l / len(indcs))
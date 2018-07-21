#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem"""

__author__ = "Filip Jankowski"

from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d['A'].append(input())
for x in range(m):
    d['B'].append(input())
for z in range(m):
    l = []
    for y in range(n):
        if d['A'][y] == d['B'][z]:
            l.append(str(y + 1))
    if len(l) != 0:
        print(" ".join(l))
    else:
        print("-1")
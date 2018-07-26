#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/maximize-it/problem"""

__author__ = "Filip Jankowski"

from itertools import product
k, m = map(int, input().split(" "))
nitab = []
for i in range(k):
    n = [int(x) for x in input().split(" ")]
    ni = n.pop(0)
    nitab.append(n)
non = list(product(*nitab))
nmax = []
for x in non:
    c = 0
    for z in x:
        c += z**2
    nmax.append(c%m)
print(max(nmax))
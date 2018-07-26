#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/py-set-add/problem"""

__author__ = "Filip Jankowski"

s = set()
n = int(input())
for i in range(n):
    s.add(input())
print(s.__len__())
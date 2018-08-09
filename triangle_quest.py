#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/python-quest-1/problem"""

__author__ = "Filip Jankowski"

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(sum(list(map(lambda x: 10**x, range(1, i)))) * i + i)
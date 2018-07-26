#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem"""

__author__ = "Filip Jankowski"

n = int(input())
ns = set(input().split(" "))
b = int(input())
bs = set(input().split(" "))
com = ns.intersection(bs).__len__()

print(str(com))
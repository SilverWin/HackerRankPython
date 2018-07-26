#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/py-set-difference-operation/problem"""

__author__ = "Filip Jankowski"

n = int(input())
ns = set(input().split(" "))
b = int(input())
bs = set(input().split(" "))
dif = ns.difference(bs).__len__()

print(str(dif))
#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/py-set-mutations/problem"""

__author__ = "Filip Jankowski"

noeA = int(input())
setA = set(input().split(" "))
n = int(input())
s = 0
for i in range(n):
    inptC, inptN = input().split(" ")
    setN = set(input().split(" "))
    if inptC == 'intersection_update':
        setA.intersection_update(setN)
    elif inptC == 'update':
        setA.update(setN)
    elif inptC == 'difference_update':
        setA.difference_update(setN)
    elif inptC == 'symmetric_difference_update':
        setA.symmetric_difference_update(setN)
for x in setA:
    s += int(x)
print(str(s))
#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/no-idea/problem"""

__author__ = "Filip Jankowski"

n, m = map(int, input().split())
arr = input().split()
a = set(input().split())
b = set(input().split())
happiness = 0
for i in arr:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1
print(str(happiness))
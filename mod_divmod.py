#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/python-mod-divmod/problem"""

__author__ = "Filip Jankowski"

a = int(input())
b = int(input())

print(a//b)
print(a%b)
print(divmod(a, b))
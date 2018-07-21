#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/itertools-product/problem"""

__author__ = "Filip Jankowski"

from itertools import product

a = [int(x) for x in input().split(" ")]
b = [int(x) for x in input().split(" ")]

axb = list(product(a, b))
axb2 = [str(x) for x in axb]

print(" ".join(axb2))
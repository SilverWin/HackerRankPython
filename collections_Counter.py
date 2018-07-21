#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/collections-counter/problem"""

__author__ = "Filip Jankowski"

from collections import Counter

x = int(input())
sizes = [int(x) for x in input().split(" ")]
n = int(input())
shoes_available = Counter(sizes)
money = 0
for i in range(n):
    offer = [int(s) for s in input().split(" ")]
    if shoes_available[offer[0]] > 0:
        money += offer[1]
        shoes_available[offer[0]] -= 1

print(str(money))
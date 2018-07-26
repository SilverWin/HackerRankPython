#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/py-collections-deque/problem"""

__author__ = "Filip Jankowski"

from collections import deque

d = deque()
n = int(input())
for i in range(n):
    command = input().split(" ")
    if command[0] == "append":
        d.append(command[1])
    elif command[0] == "pop":
        d.pop()
    elif command[0] == "popleft":
        d.popleft()
    elif command[0] == "appendleft":
        d.appendleft(command[1])
print(" ".join(d))
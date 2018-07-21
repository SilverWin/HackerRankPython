#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem"""

__author__ = "Filip Jankowski"

from collections import namedtuple
n = int(input())
s = input().split()
Students = namedtuple('Students', 'ID MARKS CLASS NAME')
marks = []
for i in range(n):
    std = input().split()
    marks.append(int(std[s.index('MARKS')]))
avrg = sum(marks) / len(marks)
print(str(avrg))
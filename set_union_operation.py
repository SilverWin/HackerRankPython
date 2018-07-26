#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/py-set-union/problem"""

__author__ = "Filip Jankowski"

n = int(input())
ns = set(input().split(" "))
b = int(input())
bs = set(input().split(" "))
print(str(ns.union(bs).__len__()))
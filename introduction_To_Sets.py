#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem"""

__author__ = "Filip Jankowski"

def average(array):
    # your code goes here
    av = sum(set(array)) / len(set(array))
    return av

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
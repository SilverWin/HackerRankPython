#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/python-lists/problem"""

__author__ = "Filip Jankowski"

if __name__ == '__main__':
    N = int(input())
    list = []
    ls = []
    for i in range(N):
        ls = input().split(" ")
        if ls[0].lower() == "insert":
            list.insert(int(ls[1]), int(ls[2]))
        elif ls[0].lower() == "print":
            print(list + "\n")
        elif ls[0].lower() == "remove":
            list.remove(int(ls[1]))
        elif ls[0].lower() == "append":
            list.append(int(ls[1]))
        elif ls[0].lower() == "sort":
            list.sort()
        elif ls[0].lower() == "pop":
            list.pop()
        elif ls[0].lower() == "reverse":
            list.reverse()

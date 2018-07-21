#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/nested-list/problem"""

__author__ = "Filip Jankowski"

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    sbg = sorted(students, key=lambda stds: stds[1])
    kf = 0
    for f in sbg:
        if f[1] == sbg[0][1]:
            kf += 1
    ks = 0
    for s in sbg:
        if s[1] == sbg[kf][1]:
            ks += 1
    tl = []
    for x in range(ks):
        tl.append([sbg[kf + x][0], sbg[kf + x][1]])
    sol = []
    for t in tl:
        sol.append(t[0])
    sol = sorted(sol)
    for o in sol:
        print(o)
        
#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/polar-coordinates/problem"""

__author__ = "Filip Jankowski"

import cmath

z = complex(input())
polarc = cmath.polar(z)
print(str(polarc[0]))
print(str(polarc[1]))

"""or
print(str(cmath.abs(z)))
print(str(cmath.phase(z)))
"""
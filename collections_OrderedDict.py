#!/usr/bin/env python

"""Solution for: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem"""

__author__ = "Filip Jankowski"

from collections import OrderedDict

n = int(input())
itemsdict = OrderedDict()
for x in range(n):
    item_name, net_price = input().rsplit(" ", maxsplit=1)
    if item_name in itemsdict:
        itemsdict[item_name] += int(net_price)
    else:
        itemsdict[item_name] = int(net_price)
for i in itemsdict:
    print(i + " " + str(itemsdict[i]))
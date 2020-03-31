#!/usr/bin/python3.6+
# -*- coding:utf-8 -*-
list = [3, 4, 1, 5, 6, 2, 7]

for i in range(len(list)):
    min = -1
    max = -1
    print("------",i)
    for a in range(i-1, -1, -1):
        if list[a] < list[i]:
            min = a
            break
    for b in range(i+1, len(list)):
        if list[b] < list[i]:
            max = b
            break
        else:
            max = -1
    print(min, max)
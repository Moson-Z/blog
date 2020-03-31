#!/usr/bin/python3.6+
# -*- coding:utf-8 -*-
import sys
if __name__ == "__main__":
    num = int(sys.stdin.readline().strip())
    list = sys.stdin.readline().strip().split()
    for i in range(num):
        min = -1
        max = -1
        print("------",i)
        for a in range(i-1, -1, -1):
            if list[a] < list[i]:
                min = a
                break
        for b in range(i+1, num):
            if list[b] < list[i]:
                max = b
                break
            else:
                max = -1
        print(min, max)
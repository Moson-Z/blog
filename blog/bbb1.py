#!/usr/bin/python3.6+
# -*- coding:utf-8 -*-
import sys
if __name__ == "__main__":
    input_num = sys.stdin.readline().strip().split()
    num = int(input_num[0])
    lens = int(input_num[1])
    print(lens)
    list = input_num[2:]
    print(list)
    ans = []
    for i in range(num):
        a = 0
        for x in range(len(list)):
            if int(list[x]) > int(list[a]):
                a = x
                pass
        ans.append(list.pop(a))
print(ans)

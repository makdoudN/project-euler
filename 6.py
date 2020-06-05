#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    sum_1 = (n * (n+1)) / 2
    sum_2 = (n * (n+1) * (2*n + 1)) / 6

    out = sum_1 ** 2 - sum_2
    print(int(out))


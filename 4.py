#!/bin/python3
# Could and should be improved ?

import sys

cache = {}
for i in range(100, 1000):
    for j in range(100, 1000):
        k = i * j
        cache[k] = 0

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for j in range(n - 1, 101100, -1):
        if j % 11 == 0 and j in cache:
            K = str(j)
            if K[0] == K[5] and K[1] == K[4] and K[2] == K[3]:
                print(j)
                break

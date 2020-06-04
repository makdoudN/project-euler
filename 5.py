#!/bin/python3

# Naive solution seems sufficient.
# TODO: See https://en.wikipedia.org/wiki/Least_common_multiple for an efficient solution.
import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    i = 1
    exit = False
    while not exit:
        for j in range(1, n+1):
            if not i % j == 0: break
            if j == n:
                print(i)
                exit = True 
        i += 1

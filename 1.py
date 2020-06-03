#!/bin/python3
import sys


def sum_1_to_k(n: int):
    return (n * (n + 1)) // 2


def sum_1_to_k_multiple_of_p(n: int, p: int):
    j = (n - 1) // p
    return p * sum_1_to_k(j)


n = 100000
sum_3 = sum_1_to_k_multiple_of_p(n, 3)
sum_5 = sum_1_to_k_multiple_of_p(n, 5)
sum_15 = sum_1_to_k_multiple_of_p(n, 15)

result = sum_3 + sum_5 - sum_15

print(result)

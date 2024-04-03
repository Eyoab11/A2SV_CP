#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    if not (1 <= n <= 1000):
        raise ValueError("Constraint violation: 1 <= n <= 1000")

    for a in arr:
        if not (-10000 <= a <= 10000):
            raise ValueError("Constraint violation: -10000 <= arr[i] <= 10000")
    last = arr[-1]
    i = n - 2  

    while i >= 0 and arr[i] > last:
        arr[i + 1] = arr[i]  
        print(" ".join(map(str, arr)))  
        i -= 1

    arr[i + 1] = last 
    print(" ".join(map(str, arr)))  


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

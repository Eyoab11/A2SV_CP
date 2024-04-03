#Sorting: Bubble Sort

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    NumberOfSwaps = 0
    if not (2<= n <= 600):
        raise ValueError("Must be in between 2<= n <= 600")
        for val in a:
            if not (1 <= val <= 2 * (10 ** 6)):
                raise ValueError("Constraint violation: 1 <= a[i] <= 2 * (10 ** 6)")

    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                NumberOfSwaps += 1

    print(f"Array is sorted in {NumberOfSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

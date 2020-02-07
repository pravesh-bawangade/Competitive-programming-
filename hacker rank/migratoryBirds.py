#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    mx = dict()
    cl = []
    for i in set(arr):
        c = arr.count(i)
        mx[i] = c
    maxx = max(mx.values())
    for key, value in mx.items():
        if value == maxx:
            cl.append(key)
    
    return min(cl)

    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

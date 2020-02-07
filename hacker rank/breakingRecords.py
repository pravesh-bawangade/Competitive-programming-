#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high = scores[0]
    low = scores[0]
    ch = 0
    cl = 0
    for i in scores:
        if i > high:
            high = i
            ch +=1
        elif i < low:
            low = i
            cl +=1
    return [ch, cl]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

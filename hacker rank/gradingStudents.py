#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    g = []
    nex = 0
    for i in grades:
        if i >= 38:
            if (i%10) > 5:
                nex = (((i//10)*10) + 10)
            else:
                nex = (((i//10)*10) + 5)
            if (nex-i) < 3:
                g.append(nex)
            else:
                g.append(i)
        else:
            g.append(i)
    return g

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

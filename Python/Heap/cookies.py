#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
from heapq import heapify, heappop, heappush

def cookies(k, A):
    # Write your code here
    heapify(A)
    res = 0
    
    while A[0] < k:
        if len(A) < 2:
            return -1
        a = heappop(A)
        b = heappop(A)
        heappush(A, a + (2*b))
        res += 1
    
    return (res if res >= 0 else -1)

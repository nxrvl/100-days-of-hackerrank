#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2:] =="AM":
        if int(s[:2]) == 12:
            return "00" + s[2:-2]
        return s[:-2]

    if int(s[:2]) == 12:
        return "12" + s[2:-2]
    return str(int(s[:2]) + 12) + s[2:-2]


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)

#!/usr/bin/env python3

#!/bin/python3

# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

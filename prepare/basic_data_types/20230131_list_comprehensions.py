#!/usr/bin/env python3

# List comprehensions are a way to create lists in a single line of code.


def list_in_lexicographical_order():
    """Return a list of all the letters in the alphabet in lexicographical order."""
    return [chr(i) for i in range(ord('a'), ord('z') + 1)]

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(list)

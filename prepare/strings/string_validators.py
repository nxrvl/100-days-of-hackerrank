#!/usr/bin/env python3

if __name__ == '__main__':
    s = input()

    for method in [str.isalnum, str.isalpha, str.isdigit,
               str.islower, str.isupper]:
        print(any(method(ch) for ch in s))

#!/usr/bin/env python3

# Works only with pypy3

if __name__ == "__main__":
    n = int(input())
    #integer_list = map(int, input().split())
    #print(integer_list)
    t = tuple(map(int, input().split()))
    print (t)
    print(hash(t))

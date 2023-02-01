#!/usr/bin/env python3

def print_formatted(number):
    # your code goes here
    #
    for i in range(1,number+1):
        b_width = number.bit_length()
        print(f'{i:>{b_width}d} {i:>{b_width}o} {i:>{b_width}x} {i:>{b_width}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#!/usr/bin/env python3
# coding: utf-8

import sys

def vomit(szam):
    sz = str(szam)
    half = int(len(sz) / 2)
    i = half
    sum = 0

    for n in sz:
        if i < len(sz):
            if n == sz[i]:
                sum = sum + int(n)
        elif i == len(sz):
            if n == sz[0]:
                sum = sum + int(n)
            i = 0
        i = i + 1
        print(n, i-1)
    return sum

def main():

    print(vomit(sys.argv[1]))

#############################################################################

if __name__ == '__main__':
    main()
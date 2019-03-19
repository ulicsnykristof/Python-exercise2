#!/usr/bin/env python3
# coding: utf-8

import sys

def vomit(szam):
    sz = str(szam)
    i = 1
    sum = 0

    for n in sz:
        if i < len(sz):
            if n == sz[i]:
                sum = sum + int(n)
        else:
            if n == sz[0]:
                sum = sum + int(n)
        i = i + 1

    return sum

def main():

    print(vomit(sys.argv[1]))

#############################################################################

if __name__ == '__main__':
    main()
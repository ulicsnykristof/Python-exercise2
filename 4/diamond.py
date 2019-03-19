#!/usr/bin/env python3
# coding: utf-8

import sys


def main():
    a = int(sys.argv[1])
    left = int((a-1) / 2)
    right = int((a-1) / 2)
    mid = 1
    out = ""
    if a % 2 == 0:
        print("paratlan szamot adj meg")
    else:
        for outer in range(a):
            for inner_left in range(left):
                out = out + " "

            for inner_mid in range(mid):
                out = out + "#"

            for inner_right in range(right):
                out = out + " "

            out = out + '\n'

            if outer < (a-1) / 2:
                left = left - 1
                right = right - 1
                mid = mid + 2
            elif outer >= (a-1) / 2:
                left = left + 1
                right = right + 1
                mid = mid - 2


    print(out)

#############################################################################

if __name__ == '__main__':
    main()
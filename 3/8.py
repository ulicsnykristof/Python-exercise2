#!/usr/bin/env python3
# coding: utf-8

import string

def dec_to_bin(num):
    i = int(num)
    bin = []
    while i > 0:
        if i % 2 == 0:
            bin.append(0)
        else:
            bin.append(1)
        i = int(i / 2)

    bin.reverse()
    return bin


def main():

    print(dec_to_bin(156))

#############################################################################

if __name__ == '__main__':
    main()
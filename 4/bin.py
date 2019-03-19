#!/usr/bin/env python3
# coding: utf-8

import string

def dec_to_bin(num):
    i = int(num)
    bin = ""
    while i > 0:
        if i % 2 == 0:
            bin = bin + '0'
        else:
            bin = bin + '1'
        i = int(i / 2)

    bin = bin + 'b0'
    bin = bin[::-1]
    return bin

def main():

    print(dec_to_bin(156))

#############################################################################

if __name__ == '__main__':
    main()
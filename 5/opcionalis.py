#!/usr/bin/env python3
# coding: utf-8

def random(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):

    sz = ''
    for outer in chars:
        for inner in text:
            if outer == inner:
                sz = sz + inner
    return sz

def main():
    print(random("999daarAB", "da"))


#############################################################################

if __name__ == '__main__':
    main()

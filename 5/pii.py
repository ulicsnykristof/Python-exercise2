#!/usr/bin/env python3
# coding: utf-8

def piertek(num):

    alter = 1
    pii = 0
    list = [n for n in range(num+1) if n % 2 != 0]
    for a in list:
        if alter == 1:
            pii = pii + (1 / a)
            alter = 0
        else:
            pii = pii - (1 / a)
            alter = 1



    return pii*4


def main():
    print(piertek(100000))


#############################################################################

if __name__ == '__main__':
    main()

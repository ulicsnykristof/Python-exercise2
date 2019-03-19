#!/usr/bin/env python3
# coding: utf-8


def main():

    list = [n for n in range(1000) if n % 3 == 0 or n % 5 == 0]
    print(sum(list))


#############################################################################

if __name__ == '__main__':
    main()
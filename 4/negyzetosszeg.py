#!/usr/bin/env python3
# coding: utf-8

import math

def main():

    n1 = 0;
    n2 = 0;

    for num in range(1,101):
        print(num)
        n1 = n1 + math.pow(num, 2)

    for num2 in range(1,101):
        n2 = n2 + num2

    print(math.pow(n2, 2)-n1)


#############################################################################

if __name__ == '__main__':
    main()
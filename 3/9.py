#!/usr/bin/env python3
# coding: utf-8

import string


def main():

   summa = 0
   for i in range(1000):
       if i % 3 == 0 or i % 5 == 0:
           summa = summa + i

   print(summa)

#############################################################################

if __name__ == '__main__':
    main()
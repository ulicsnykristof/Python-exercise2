#!/usr/bin/env python3
# coding: utf-8

import sys

def what(val1, val2):

    if bool(val1) == True & bool(val2) == True:
        return False
    elif bool(val1) == False & bool(val2) == False:
        return False
    else:
        return True


def main():

    print(what("python", None))

#############################################################################

if __name__ == '__main__':
    main()
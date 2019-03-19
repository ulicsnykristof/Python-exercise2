#!/usr/bin/env python3
# coding: utf-8


def fordito(n):
    asd = str(n)
    asd = asd[::-1]
    return int(asd)

#mashogy:

def fordito2(n):
	return int(str(n)[::-1])

def main():
    print(fordito2(1235432))

#############################################################################

if __name__ == '__main__':
    main()
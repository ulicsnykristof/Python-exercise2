#!/usr/bin/env python3
# coding: utf-8

import sys

MELY = "aáoóuú"
MAGAS = "eéiíöőüű"


def hangrend(word):

    magas = 0
    mely = 0

    for outer in word:
        for inner_mely in MELY:
            if outer == inner_mely:
                mely = mely + 1

        for inner_magas in MAGAS:
            if outer == inner_magas:
                magas = magas + 1


    if mely == 0 and magas > 0:
        print(mely, magas)
        return "Magas hangrendű szó"
    elif mely > 0 and magas == 0:
        print(mely, magas)
        return "Mély hangrendű szó"
    else:
        print(mely, magas)
        return "Vegyes hangrendű szó"

def main():

    print(hangrend(sys.argv[1]))

#############################################################################

if __name__ == '__main__':
    main()
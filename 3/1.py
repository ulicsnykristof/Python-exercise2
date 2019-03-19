#!/usr/bin/env python3
# coding: utf-8

def osszead(lista):
    szorzat = 1;
    if len(lista) == 0:
        return 1
    else:
        for idx in lista:
            szorzat = lista[idx-1] * szorzat
        return szorzat

def main():

    asd = [1, 2, 3, 4, 5]
    print(osszead(asd))

#############################################################################

if __name__ == '__main__':
    main()
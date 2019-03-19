#!/usr/bin/env python3
# coding: utf-8

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def main():

    s = TEXT
    ns = ""

    for i in range(106):
        if ord(s[i]) == 121:
            ns = ns + "a"
        elif ord(s[i]) == 89:
            ns = ns + "A"
        elif 64 < ord(s[i]) < 122:
            ns = ns + chr(ord(s[i]) + 2)
        elif ord(s[i]) == 32:
            ns = ns + " "
        elif ord(s[i]) == 10:
            ns = ns + '\n'
        elif ord(s[i]) == 58:
            ns = ns + ':'
        elif ord(s[i]) == 33:
            ns = ns + '!'

    print(ns)

#############################################################################

if __name__ == '__main__':
    main()
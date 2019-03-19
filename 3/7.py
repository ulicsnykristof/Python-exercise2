#!/usr/bin/env python3
# coding: utf-8

import string

def remove_whitespaces(st):
    st2 = st.replace("\n", "")
    return st2


def main():

    for i in range(94):
        print(i+33, ": ", chr(i+33), sep="")


#############################################################################

if __name__ == '__main__':
    main()
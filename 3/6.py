#!/usr/bin/env python3
# coding: utf-8

import string

def remove_whitespaces(st):
    st2 = st.replace("\n", "")
    return st2


def main():

    print(remove_whitespaces("192.20.246.138:\n 6666"))



#############################################################################

if __name__ == '__main__':
    main()
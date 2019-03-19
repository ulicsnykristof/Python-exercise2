#!/usr/bin/env python3
# coding: utf-8


def main():
    # 1
    list = ['auto', 'villamos', 'metro']
    nlist = [n.upper() + '!' for n in list]
    print(list)
    print(nlist)
    print()

    # 2
    list = ['aladar', 'bela', 'csenge']
    nlist = [n.capitalize() + '!' for n in list]
    print(list)
    print(nlist)
    print()

    # 3
    nlist = [0 for n in range(10)]
    print(nlist)

    # 4
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nlist = [n + n for n in list]
    print(list)
    print(nlist)
    print()

    # 5
    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    nlist = [int(n) for n in list]
    print(list)
    print(nlist)
    print()

    # 6
    list = "1234567"
    nlist = [int(n) for n in list]
    print(list)
    print(nlist)
    print()

    # 7
    list = 'random beírt blbabla szöveg a aa aaa'
    nlist = [len(n) for n in list.rsplit(" ")]
    print(list)
    print(nlist)
    print()

    # 8
    list = 'random beírt blbabla szöveg a aa aaa'
    nlist = [n[:1] for n in list.rsplit(" ")]
    print(list)
    print(nlist)
    print()

    # 9
    list = 'random beírt blbabla szöveg a aa aaa'
    nlist = [(n, len(n)) for n in list.rsplit(" ")]
    print(list)
    print(nlist)
    print()

    # 10
    list = [n for n in range(10) if n % 2 == 0]
    print(list)
    print()

    # 11
    list = [n ** 2 for n in range(20) if n % 2 == 0]
    print(list)
    print()

    # 12
    list = [n ** 2 for n in range(20) if str(n ** 2)[-1] == '4']
    print(list)
    print()

    # 13
    list = ''.join([chr(n) for n in range(65, 91)])
    print(list)
    print()

    # 14
    list = [' asdasd ', '  dsaasd   ', '  sadsa ']
    nlist = [n.strip() for n in list]
    print(list)
    print(nlist)
    print()

    # 15
    list = [1 ,0, 1, 0, 0, 0, 1, 1]
    st = ''.join([str(n) for n in list])
    print(list)
    print(st)
    print()

#############################################################################

if __name__ == '__main__':
    main()
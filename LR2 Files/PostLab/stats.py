"""
Author: Gilroy Sio, and Modified by Rence Cadsawan
File: stats.py
"""

import statistics as st

def mean(arg="numbers.txt"):
    try:
        f = open(arg, 'r')
    except:
        f = open(input("Input file name: "), 'r')
    num = [int(i) for i in f.readlines()]
    f.close()
    if len(num) == 0:
        return 0
    return st.mean(num)

def mode(arg="numbers.txt"):
    try:
        f = open(arg, 'r')
    except:
        f = open(input("Input file name: "), 'r')
    num = [int(i) for i in f.readlines()]
    f.close()
    if len(num) == 0:
        return 0
    return st.mode(num)

def median(arg="numbers.txt"):
    try:
        f = open(arg, 'r')
    except:
        f = open(input("Input file name: "), 'r')
    num = [int(i) for i in f.readlines()]
    f.close()
    if len(num) == 0:
        return 0
    return st.median(num)

def main():
    print(mean())
    print(mode())
    print(median())

if __name__ == "__main__":
    main()
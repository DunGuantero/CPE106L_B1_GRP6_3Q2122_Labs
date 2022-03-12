"""
Author: Gilroy Sio
File: LR2_2.py
"""

f = open(input("Input file name: "), 'r')
lines = [i.strip() for i in f.readlines()]
f.close()
while(True):
    index = int(input("Enter line to read:"))-1
    if index==-1:
        break
    try:
        print(lines[index])
    except:
        print("Index out of bounds")

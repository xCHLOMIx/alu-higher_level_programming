#!/usr/bin/env python3
islower = __import__('7-islower').islower
def islower(letter):
    if letter.islower():
        print f"{letter} is lower"
    else:
        print f"{letter} is upper"

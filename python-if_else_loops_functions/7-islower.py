#!/usr/bin/python3
def islower(letter):
    if ord(letter) < 122 or ord(letter) > 97:
        return True
    elif ord(letter) > 90 or ord(letter) < 65:
        return False


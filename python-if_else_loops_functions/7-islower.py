#!/usr/bin/python3
def islower(letter):
    if chr(letter) > 122 or chr(letter) < 97:
        return True
    else:
        return False

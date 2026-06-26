#!/usr/bin/python3
def islower(letter):
    if int(chr(letter)) > 122 or int(chr(letter)) < 97:
        return True
    else:
        return False

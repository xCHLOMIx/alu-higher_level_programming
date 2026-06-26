#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        return str(number)[-1]
    else:
        return str((number * -1))[-1]

#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        print(str(number)[-1])
        return str(number)[-1] + str(number)[-1]
    else:
        print(str((number * -1))[-1])
        return str((number * -1))[-1] + str(number)[-1]

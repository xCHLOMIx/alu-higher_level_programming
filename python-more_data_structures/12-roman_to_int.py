#!/usr/bin/python3
def roman_to_int(roman_string):
    m = 0
    c = 0
    x = 0
    i = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    if "M" in roman_string:
        m = 1000
    if "MM" in roman_string:
        m = 2000
    if "MMM" in roman_string:
        m = 3000
    if "C" in roman_string:
        if "XC" in roman_string:
            c = 0
        elif "CXC" in roman_string:
            c = 100
        else:
            c = 100
    if "CC" in roman_string:
        c = 200
    if "CCC" in roman_string:
        c = 300
    if "CD" in roman_string:
        c = 400
    if "D" in roman_string:
        c = 500
    if "DC" in roman_string:
        c = 600
    if "DCC" in roman_string:
        c = 700
    if "DCCC" in roman_string:
        c = 800
    if "CM" in roman_string:
        c = 900
    if "X" in roman_string:
        if "IX" in roman_string:
            x = 0
        elif "XIX" in roman_string:
            x = 10
        else:
            x = 10
    if "XX" in roman_string:
        x = 20
    if "XXX" in roman_string:
        x = 30
    if "XL" in roman_string:
        x = 40
    if "L" in roman_string:
        x = 50
    if "LX" in roman_string:
        x = 60
    if "LXX" in roman_string:
        x = 70
    if "LXXX" in roman_string:
        x = 80
    if "XC" in roman_string:
        x = 90
    if "I" in roman_string:
        i = 1
    if "II" in roman_string:
        i = 2
    if "III" in roman_string:
        i = 3
    if "V" in roman_string:
        i = 5
    if "IV" in roman_string:
        i = 4
    if "VI" in roman_string:
        i = 6
    if "VII" in roman_string:
        i = 7
    if "VIII" in roman_string:
        i = 8
    if "IX" in roman_string:
        i = 9
    return m + c + x + i

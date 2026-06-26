#!/usr/bin/python3
def uppercase(str):
    final = ""

    for i in str.lower():
        if i == " ":
            final += i
            continue
        if ord(i) >= 48 and ord(i) <= 57:
            final += i
            continue
        upper = ord(i) - 32
        final += chr(upper)
    print("{}".format(final))

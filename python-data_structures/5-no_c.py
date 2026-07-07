#!/usr/bin/python3
def no_c(my_string):
    arr = []
    c = []
    for letter in my_string:
        arr.append(letter)
    for i in arr:
        if i.lower() == "c":
            c.append(i)
    for i in c:
        arr.pop(arr.index(i))
    return "".join(arr)

#!/usr/bin/python3
def no_c(my_string):
    arr = []
    index = 0
    for i in my_string:
        arr.append(i)
    for i in arr:
        if i == "C" or i == "c":
            arr.pop(index)
        index += 1
    return "".join(arr)

#!/usr/bin/python3
def no_c(my_string):
    arr = []
    c = []
    for letter in my_string:
        arr.append(letter)
    for i in arr:
        if i.lower() == "c":
            c.append(i)
            print(c)
    for i in c:
        arr.pop(arr.index(i))
    return "".join(arr)
print(no_c("HellcCcccooccoscccss"))

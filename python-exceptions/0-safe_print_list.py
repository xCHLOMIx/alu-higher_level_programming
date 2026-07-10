#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = ''
    r = 1
    try:
        for i in range(x):
            a += str(my_list[i])
            r += 1
    except IndexError:
        pass
    print(a)
    return int(r)

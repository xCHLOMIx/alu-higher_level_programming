#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = ''
    try:
        for i in range(x):
            a += str(my_list[i])
    except IndexError:
        pass
    print(a)
    return int(x)
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    z = []
    for a, b in a_dictionary.items():
        z.append([a, b * 2])
    return dict(z)

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def r(a):
        if a == search:
            return replace
        else:
            return a
    return list(map(r, my_list))

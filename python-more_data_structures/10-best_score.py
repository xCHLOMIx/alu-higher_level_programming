#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a = list(a_dictionary.values())
    top = sorted(a)[-1]
    for b, c in a_dictionary.items():
        if c == top:
            return b

#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if i == j:
            continue
        if i < 5 and int(str(i) + str(j)) > int(str(j) + str(i)) and j + i == i + j:
            continue
        if i >= 5 and int(str(i) + str(j)) > int(str(j) + str(i)) and j + i == i + j:
            continue
        if i == 8 and j == 9:
            print("{}{}".format(i, j), end="\n")
            continue
        print("{}{}".format(i, j), end=", ")

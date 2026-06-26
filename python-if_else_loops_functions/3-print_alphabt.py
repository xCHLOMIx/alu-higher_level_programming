#!/usr/bin/python3
for i in range(65, 91):
    if i == 81 or i == 69:
        continue
    print("{}".format(chr(i).lower()), end="")

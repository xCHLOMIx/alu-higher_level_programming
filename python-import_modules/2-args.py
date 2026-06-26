#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv

    if len(args) - 1 > 1:
        print("{} arguments:".format(len(args) - 1))
    else:
        print("{} argument:".format(len(args) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))

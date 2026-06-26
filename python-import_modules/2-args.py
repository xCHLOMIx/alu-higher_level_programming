#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    print("{} arguments:".format(len(args) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))

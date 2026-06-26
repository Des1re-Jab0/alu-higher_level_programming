#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{}".format(chr(ord(c) - 32 * (96 < ord(c) < 123))), end="")
    print("")

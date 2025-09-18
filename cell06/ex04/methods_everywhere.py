#!/usr/bin/env python3
import sys

def shrink(s):
    return s[:8]

def enlarge(s):
    return s + "Z" * (8 - len(s))

args = sys.argv[1:]

if len(args) < 1:
    print("none")
else:
    for arg in args:
        if len(arg) > 8:
            print(shrink(arg))
        elif len(arg) < 8:
            print(enlarge(arg))
        else:
            print(arg)

#!/usr/bin/env python3
import sys

def downcase_it(s: str) -> str:
    return s.lower()

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for arg in args:
        print(downcase_it(arg))


#!/usr/bin/env python3
import sys

args = sys.argv[1:]   

if len(args) == 1:
    print(args[0].lower())  
else:
    print("none")

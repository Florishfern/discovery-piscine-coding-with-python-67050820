#!/usr/bin/env python3
import sys
import re

args = sys.argv[1:]  
if len(args) != 2:
    print("none")
else:
    keyword = args[0]
    text = args[1]
    matches = re.findall(keyword, text)
    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))

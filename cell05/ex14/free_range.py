#!/usr/bin/env python3
import sys

# ต้องมีพารามิเตอร์ 2 ตัวเท่านั้น
if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    numbers = list(range(start, end + 1))
    print(numbers)

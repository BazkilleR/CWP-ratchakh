#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    result = ""
    for char in sys.argv[1]:
        if char == "z":
            result += "z"
    print(result if result else "none")

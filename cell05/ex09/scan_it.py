#!/usr/bin/env python3
import sys

if len(sys.argv) != 3 or not sys.argv[1] or sys.argv[1] not in sys.argv[2]:
    print("none")
else:
    print(sys.argv[2].count(sys.argv[1]))
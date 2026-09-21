#!/usr/bin/env python3
import sys


def shrink(word):
    print(word[:8])


def enlarge(word):
    print(word + "Z" * (8 - len(word)))


if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)

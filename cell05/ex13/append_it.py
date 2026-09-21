#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        match param:
            case _ if param.endswith("ism"):
                continue
            case _:
                print(param + "ism")

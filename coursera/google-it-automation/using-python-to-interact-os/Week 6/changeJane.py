#!/usr/bin/env python3

import sys
import subprocess

print(sys.argv[1])

with open(sys.argv[1]) as file:
        changed = file.read().replace('jane', 'jdoe')
        file.seek(0)
        original = file.read()
        print(original)
        print(changed)
        for f, fo in zip(changed.split('\n'), original.split('\n')):
               print(f)
               print(fo)
               try:
                        subprocess.run(["mv", ".."+fo, ".."+f])
               except:
                        print('! file does not exist')
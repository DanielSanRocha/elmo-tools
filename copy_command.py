import sys

import clipboard

if sys.stdin.isatty():
    raise Exception("You need to pipe some command to this command!")


full = []
while True:
    line = sys.stdin.readline()
    if not line:
        break
    full.append(line.rstrip())

clipboard.copy("\n".join(full))

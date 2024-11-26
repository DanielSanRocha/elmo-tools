import argparse
import os

from humanfriendly import format_size, parse_size


def calculate(path):
    if os.path.islink(path):
        return 0
    elif os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total = 0
        for p in os.listdir(path):
            abs_p = os.path.abspath(os.path.join(path, p))
            total += calculate(abs_p)
        return total
    return 0


parser = argparse.ArgumentParser(
    prog="size", description="List all sizes of folders or files on this directory."
)
parser.add_argument("path", nargs="?", type=str, default=".", help="Path to analyze.")
parser.add_argument(
    "--cut", type=str, default="0B", help="Minimum size to be displayed.", nargs="?"
)

args = parser.parse_args()
path = os.path.abspath(args.path)
cut = parse_size(args.cut)

if os.path.islink(path):
    pass
elif os.path.isfile(path):
    size = calculate(path)
    if size >= cut:
        print(f"{args.path}: {format_size(size)}")
elif os.path.isdir(path):
    for p in os.listdir(path):
        abs_p = os.path.abspath(os.path.join(path, p))
        if os.path.islink(abs_p):
            continue
        size = calculate(abs_p)
        if size >= cut:
            print(f"{p}: {format_size(size)}")

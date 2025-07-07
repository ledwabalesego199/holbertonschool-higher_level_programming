#!/usr/bin/env python3

if __name__ == "__main__":
    from sys import argv

    count = len(argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")

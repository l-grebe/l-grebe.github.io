#!/usr/bin/env python3
import os

def gen_row(show_name: str, file_path: str, level: int):
    return "{}* [{}]({})\n".format("  " * level, show_name, file_path)

def list_files(path, level):
    lsdir = os.listdir(path).sort()
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for d in dirs:
        yield d
        list_files(os.path.join(path, d), level + 1)
    for f in files:
        yield f

def main():
    for name in list_files('.', 0):
        print(name)

if __name__ == '__main__':
    main()

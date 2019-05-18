#!/usr/bin/env python

import argparse

from pathlib import Path

def rename(dname, fname):
    d = Path(dname).resolve()
    files = [f for f in d.iterdir() if f.is_file()]
    files = sorted(files, key=lambda f: f.stat().st_ctime)
    for i,f in enumerate(files):
        f.rename(f.with_name(fname + "-" + str(i)).with_suffix(f.suffix))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='rename and enumerate files in directory.')
    parser.add_argument('--dir', nargs='?', type=str)
    parser.add_argument('--name', nargs='?', type=str)
    args = parser.parse_args()

    rename(args.dir, args.name)

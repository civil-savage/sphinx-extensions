#!usr/bin/python3

import argparse
import os
import re
import shutil
import sys

SOURCE = "src directory"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('index', default=None, type=str, nargs='?',
                        help='Name of the documentation')
    args = parser.parse_args()
    if args.index:
        populate_index()

def populate_index():
    if os.path.isfile('index.rst'):
        fname = 'index.rst'
    else:
        fname = 'index.rst.gen'
    rst_files = []
    for d in os.walk('.'):
        for f in d[2]:
            if os.path.splitext(f)[-1].lower() == '.rst':
                rst_files.append(os.path.join(d[0],f))
                print(rst_files.pop(0))
    
     with open(os.path.join(SOURCE, 'index.rst'), 'w') as wfile:
         wfile.write(rst_files)


if __name__ == '__main__':
    main()




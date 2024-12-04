from sys import argv as a
from datetime import date
import os.path as p

if len(a) != 2:
    d = date.today().day
else:
    d = int(a[1])

codefile = f"12-{d:02d}-2024.py"
inputfile = f"inputs/12{d:02d}.txt"

if not p.exists(codefile):
    with open(codefile, "w") as f:
        f.write("from utils import *\n\n## part 1\nwith open(FILENAME, 'r') as f:\n\tpass\n\n## part 2\nwith open(FILENAME, 'r') as f:\n\tpass")

if not p.exists(inputfile):
    with open(inputfile, "a") as _:
        pass
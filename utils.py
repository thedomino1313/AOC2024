from functools import *
from itertools import *
from collections import Counter, defaultdict
import regex as re, math
import sys
from copy import deepcopy
from operator import add, mul, sub

FILENAME = f"inputs/{"".join(sys.argv[0].split("-")[:2])}.txt"

class Coord(tuple):
    def __add__(self, val):
        if type(val) == Coord:
            return Coord(starmap(add, zip(self, val)))
        else:
            return Coord(map(lambda x:add(x, val), self))
    
    def __sub__(self, val):
        if type(val) == Coord:
            return Coord(starmap(sub, zip(self, val)))
        else:
            return Coord(map(lambda x:sub(x, val), self))
    
    def __mul__(self, val):
        if type(val) == Coord:
            return sum(starmap(mul, zip(self, val)))
        else:
            return Coord(map(lambda x:mul(x, val), self))
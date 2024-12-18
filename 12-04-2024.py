from utils import *

with open(FILENAME, 'r') as f:
    text = list(map(lambda x: list(x.strip()), f.readlines()))

## part 1
def search(text, posx, posy, dir_=(), letter = 0):
    string = "XMAS"
    if letter == 4: return 1
    if 0 > posx or posx >= len(text) or 0 > posy or posy >= len(text[0]): return 0
    if not dir_:
        return sum(search(text, posx+i, posy+j, (i,j), 1) for i,j in product([-1, 0, 1], repeat=2) if i or j)
    if text[posx][posy] == string[letter]:
            return search(text, posx+dir_[0], posy+dir_[1], dir_, letter+1)
    return 0

print(sum(search(text, i, j) for i in range(len(text)) for j in range(len(text[0])) if text[i][j] == "X"))

## part 2
def search(text, posx, posy):
    return set((text[posx-1][posy-1], text[posx+1][posy+1])) == set("MS") == set((text[posx+1][posy-1], text[posx-1][posy+1]))

print(sum(search(text, i, j) for i in range(1, len(text[1:])) for j in range(1, len(text[0][1:])) if text[i][j] == "A"))

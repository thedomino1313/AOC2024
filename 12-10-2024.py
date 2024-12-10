from utils import *

def search(posx, posy, data, graph, ends):
    if (val := data[posx][posy]) == 9:
        ends[0].add((posx,posy))
        ends[1].append((posx,posy))
    else:
        list(search(x, y, data, graph, ends) for x,y in graph[(posx,posy)] if data[x][y] == val + 1)            

with open(FILENAME, 'r') as f:
    data = list(map(lambda x: list(map(int, list(x.strip()))),  f))

graph = {(posx,posy): [(posx+i, posy+j) for i,j in [(-1,0),(1,0),(0,-1),(0,1)] if 0 <= posx+i < len(data) and 0 <= posy+j < len(data[0])] for posx in range(len(data)) for posy in range(len(data[0]))}
starts = {(posx,posy): (set(), list()) for posx in range(len(data)) for posy in range(len(data[0])) if data[posx][posy] == 0}
list(search(x,y,data,graph,starts[(x,y)]) for x,y in starts)
print(reduce(lambda x,y: (x[0] + len(y[0]), x[1] + len(y[1])), starts.values(), (0,0)))

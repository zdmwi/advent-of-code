import sys
from pprint import pprint


def get_neighbours(coords, y_max, x_max):
  i, j = coords

  n = (i-1, j) if i-1 >= 0 else None
  ne = (i-1, j+1) if i-1 >= 0 and j+1 < x_max else None
  e = (i, j+1) if  j+1 < x_max else None
  se = (i+1, j+1) if i+1 < y_max and j+1 < x_max else None
  s = (i+1, j) if i+1 < y_max else None
  sw = (i+1, j-1) if i+1 < y_max and j-1 >= 0 else None
  w = (i, j-1) if j-1 >= 0 else None
  nw = (i-1, j-1) if i-1 >= 0 and j-1 >= 0 else None

  return list(filter(lambda x: x is not None, [n, ne, e, se, s, sw, w, nw]))

  
def solve(graph):
  y_max = len(graph)
  x_max = len(graph[0])

  flashes = 0
  steps = 100
  for _ in range(steps):
    to_flash = set()
    for i in range(y_max):
      for j in range(x_max):
        graph[i][j] += 1
        if graph[i][j] > 9:
          to_flash.add((i, j))

    flashed = set()
    for i, j in to_flash:
      queue = [(i, j)]

      while len(queue) > 0:
        current = queue.pop(0)

        if current in flashed:
          continue

        y, x = current
        if graph[y][x] > 9:
          graph[y][x] = 0
          flashes += 1
          flashed.add(current)
          nbrs = get_neighbours((y, x), y_max, x_max)
          for nbr in nbrs:
            if nbr not in flashed: 
              y_n, x_n = nbr
              graph[y_n][x_n] += 1
              if graph[y_n][x_n] > 9:
                queue.append(nbr)

  return flashes


if __name__ == '__main__':
  graph = [[int(ch) for ch in line.strip()] for line in sys.stdin.readlines()]

  ans = solve(graph)
  print(ans)
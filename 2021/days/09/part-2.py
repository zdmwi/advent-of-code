import sys
import math
from pprint import pprint
from functools import reduce

def get_neighbours(graph, coords):
  y_max = len(graph)
  x_max = len(graph[0])

  i, j = coords
  up = (i+1, j) if i+1 < y_max else None
  right = (i, j+1) if j + 1 < x_max else None
  down = (i-1, j) if i-1 >= 0 else None
  left = (i, j-1) if j - 1 >= 0 else None

  return filter(lambda x: x is not None, [up, right, down, left])


def calculate_risk_level(heightmap):
  y_max = len(heightmap)
  x_max = len(heightmap[0])

  low_points = set()
  for i in range(y_max):
    for j in range(x_max):
      current = heightmap[i][j]
      nbrs = get_neighbours(heightmap, (i, j))

      lowest = True
      for y, x in nbrs:
        if current >= heightmap[y][x]:
          lowest = False
          break

      if lowest:
        low_points.add((i, j))

  basin_sizes = []
  for i, j in low_points:
    basin_size = 0
    basin = set()
    stack = []

    stack.append((i, j))

    seen = set()
    while len(stack) > 0:
      current = stack.pop()

      if current in seen:
        continue

      basin_size += 1

      seen.add(current)

      neighbours = get_neighbours(heightmap, current)
      for nbr in neighbours:
        if nbr not in seen and heightmap[nbr[0]][nbr[1]] != 9:
          stack.append(nbr)

    basin_sizes.append(basin_size)

  return reduce(lambda x, y: x * y, sorted(basin_sizes, reverse=True)[:3])


if __name__ == '__main__':
  heightmap = [[int(x) for x in line.strip()] for line in sys.stdin.readlines()]

  ans = calculate_risk_level(heightmap)
  print(ans)
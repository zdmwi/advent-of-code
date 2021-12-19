import sys
import heapq
import math
from collections import defaultdict
from pprint import pprint

def display_graph(graph):
  print("\n".join("".join(list(map(str, line))) for line in graph))

def get_neighbours(coords, y_max, x_max):
  i, j = coords

  n = (i-1, j) if i-1 >= 0 else None
  e = (i, j+1) if j+1 < x_max else None
  s = (i+1, j) if i+1 < y_max else None
  w = (i, j-1) if j-1 >= 0 else None

  return list(filter(lambda x: x is not None, [n, e, s, w]))


def expand_cave(cave):
  y_max = len(cave)
  x_max = len(cave[0])
  new_y_max = y_max * 5
  new_x_max = x_max * 5

  matrix = [[i+j for j in range(5)] for i in range(5)]

  expanded_cave = [[0 for _ in range(new_x_max)] for _ in range(new_y_max)]

  y_reps = 0
  for i in range(new_y_max):
    if i != 0 and i % y_max == 0:
      y_reps += 1
    x_reps = 0
    for j in range(new_x_max):
      if j != 0 and j % x_max == 0:
        x_reps += 1
      
      risk = cave[i%y_max][j%x_max] + matrix[y_reps][x_reps]
      if risk > 9:
        risk = risk % 10 + 1
      expanded_cave[i][j] = risk

  return expanded_cave


def find_safest_path(cave):
  cave = expand_cave(cave)

  y_max = len(cave)
  x_max = len(cave[0])
  
  risk_levels = defaultdict(lambda: math.inf)
  risk_levels[(0, 0)] = 0

  visited = set()
  pq = []
  heapq.heappush(pq, (0, (0, 0)))
  while pq:
    risk, coords = heapq.heappop(pq)

    visited.add(coords)
    
    if coords == (y_max-1, x_max-1):
      return risk

    for nbr in get_neighbours(coords, y_max, x_max):
      yn, xn = nbr
      if nbr not in visited:
        new_risk = risk + cave[yn][xn]
        if new_risk < risk_levels[nbr]:
          heapq.heappush(pq, (new_risk, nbr))
          risk_levels[nbr] = new_risk

if __name__ == '__main__':
  cave = [list(map(int, line.strip())) for line in sys.stdin.readlines()]

  ans = find_safest_path(cave)
  print(ans)
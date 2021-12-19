import sys
import heapq
import math
from collections import defaultdict
from pprint import pprint

def get_neighbours(coords, y_max, x_max):
  i, j = coords

  n = (i-1, j) if i-1 >= 0 else None
  e = (i, j+1) if j+1 < x_max else None
  s = (i+1, j) if i+1 < y_max else None
  w = (i, j-1) if j-1 >= 0 else None

  return list(filter(lambda x: x is not None, [n, e, s, w]))


def find_safest_path(cave):
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
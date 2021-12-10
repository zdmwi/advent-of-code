import sys
import math
from pprint import pprint

def calculate_risk_level(heightmap):
  y_max = len(heightmap)
  x_max = len(heightmap[0])

  low_points = set()
  for i in range(y_max):
    for j in range(x_max):
      current = heightmap[i][j]
      left = heightmap[i][j-1] if j - 1 >= 0 else math.inf
      right = heightmap[i][j+1] if j + 1 < x_max else math.inf
      up = heightmap[i+1][j] if i+1 < y_max else math.inf
      down = heightmap[i-1][j] if i-1 >= 0 else math.inf
      
      if current < right and current < left and \
          current < up and current < down:
          low_points.add((i, j))

  return sum([heightmap[i][j] + 1 for i,j in low_points])


if __name__ == '__main__':
  heightmap = [[int(x) for x in line.strip()] for line in sys.stdin.readlines()]

  ans = calculate_risk_level(heightmap)
  print(ans)
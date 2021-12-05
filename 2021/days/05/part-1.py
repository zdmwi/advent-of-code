import sys
from collections import Counter

def x1(line):
  return line[0][0]

def x2(line):
  return line[1][0]

def y1(line):
  return line[0][1]

def y2(line):
  return line[1][1]

def is_vertical(line):
  return x1(line) == x2(line)

def is_horizontal(line):
  return y1(line) == y2(line)

def is_colinear(l1, l2):
  return (x1(l1) == x2(l1) == x1(l2) == x2(l2)) \
    or (y1(l1) == y2(l1) == y1(l2) == y2(l2))

def is_diagonal(line):
  return not is_horizontal(line) and not is_vertical(line)

def count_overlapping_points(lines):
  hits = Counter()

  counted = set()
  for line in lines:
    if is_diagonal(line):
      continue

    for y in range(min(y1(line), y2(line)), max(y1(line), y2(line))+1):
      for x in range(min(x1(line), x2(line)), max(x1(line), x2(line))+1):
        key = f'{x},{y}'
        hits[key] += 1
        if key not in counted and hits[key] >= 2:
          counted.add(key)

  return len(counted)


if __name__ == '__main__':
  lines = [
    [list(map(int, point.split(','))) for point in line.strip().split('->')] 
    for line in sys.stdin.readlines()
  ]
  
  ans = count_overlapping_points(lines)
  print(ans)
import sys

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
  max_x = max(max(line[0][0], line[1][0]) for line in lines)
  max_y = max(max(line[0][1], line[1][1]) for line in lines)

  board = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

  counted = set()
  for line in lines:
    if is_diagonal(line):
      x_step = 1
      y_step = 1
      if x1(line) > x2(line):
        x_step = -1

      if y1(line) > y2(line):
        y_step = -1

      x = x1(line)
      y = y1(line)
      board[y][x] += 1
      key = f'{x},{y}'
      if key not in counted and board[y][x] >= 2:
        counted.add(key)
      while x != x2(line) and y != y2(line):
        x += x_step
        y += y_step
        board[y][x] += 1
        
        key = f'{x},{y}'
        if key not in counted and board[y][x] >= 2:
          counted.add(key)
      
    else:
      lower_y = min(y1(line), y2(line))
      upper_y = max(y1(line), y2(line))
      lower_x = min(x1(line), x2(line))
      upper_x = max(x1(line), x2(line))
      for y in range(lower_y, upper_y + 1):
        for x in range(lower_x, upper_x + 1):
          board[y][x] += 1
          key = f'{x},{y}'
          if key not in counted and board[y][x] >= 2:
            counted.add(key)

  return len(counted)


if __name__ == '__main__':
  lines = [
    [list(map(int, point.split(','))) for point in line.strip().split('->')] 
    for line in sys.stdin.readlines()
  ]
  
  ans = count_overlapping_points(lines)
  print(ans)
import sys

def display_paper(dots):
  y_max = 0
  x_max = 0
  for y, x in dots:
    if y > y_max:
      y_max = y
    if x > x_max:
      x_max = x

  paper = [['.' for _ in range(x_max+1)] for _ in range(y_max+1)]

  for y, x in dots:
    paper[y][x] = '#'

  print("\n".join("".join(line) for line in paper))

def find_code(dots, instructions):
  steps_to_complete = 1
  count = len(dots)

  for instruction in instructions[:steps_to_complete]:
    axis, crease = instruction.split('=')
    crease = int(crease)
    if axis == 'y':
      temp = dots.copy()
      for dot in temp:
        y, x = dot
        if y > crease:
          dy = y - (y - crease) * 2
          if (dy, x) in dots:
            count -= 1
          dots.remove(dot)
          dots.add((dy, x))

    elif axis == 'x':
      temp = dots.copy()
      for dot in temp:
        y, x = dot
        if x > crease:
          dx = x - (x - crease) * 2
          if (y, dx) in dots:
            count -= 1
          dots.remove(dot)
          dots.add((y, dx))

  display_paper(dots)
  return count
  


if __name__ == '__main__':
  dots = set()
  instructions = []
  getting_instructions = False
  for line in sys.stdin.readlines():
    if len(line.strip()) == 0:
      getting_instructions = True
      continue
    if getting_instructions:
      instructions.append(line.strip().split()[-1])
    else:
      x, y = map(int, line.strip().split(','))
      dots.add((y, x))

  ans = find_code(dots, instructions)
  print(ans)


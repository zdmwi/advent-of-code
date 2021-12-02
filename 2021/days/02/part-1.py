import sys

def get_planned_location(cmds):
  x = 0
  y = 0
  for direction, magnitude in cmds:
    magnitude = int(magnitude)
    if direction == 'forward':
      x += magnitude
    elif direction == 'down':
      y += magnitude
    elif direction == 'up':
      y -= magnitude

  return x, y
    

if __name__ == '__main__':
  lines = sys.stdin.readlines()
  cmds = [line.strip().split() for line in lines]

  loc = get_planned_location(cmds)
  print(loc)
  print(loc[0] * loc[1])
import sys


def simulate(xb, yb, vx, vy):
  x, y = 0, 0
  count = 0

  max_steps = 2 * abs(yb[0]) + 1
  for _ in range(max_steps + 1):
    x += vx
    y += vy

    if xb[0] <= x <= xb[1] and yb[0] <= y <= yb[1]:
      count += 1
      break
    elif x > xb[1] or y < yb[0]:
      break

    if vx > 0:
      vx -= 1
    elif vx < 0:
      vx += 1
    vy -= 1

  return count


def find_trajectory(x, y):
  count = 0
  for vy in range(y[0], abs(y[0])):
    for vx in range(1, x[1] + 1):
      count += simulate(x, y, vx, vy)

  return count


if __name__ == '__main__':
  _, _, x, y = sys.stdin.readline().strip().split()
  
  x1, x2 = map(int, x[2:-1].split('..'))
  y1, y2 = map(int, y[2:].split('..'))

  ans = find_trajectory((x1, x2), (y1, y2))
  print(ans)
  
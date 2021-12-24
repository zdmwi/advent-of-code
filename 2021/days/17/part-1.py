import sys
import math

def simulate(xb, yb, vx, vy):
  x, y = 0, 0
  max_y = -math.inf

  max_steps = 2 * abs(yb[0]) + 1
  for _ in range(max_steps + 1):
    x += vx
    y += vy
    max_y = max(max_y, y)

    if xb[0] <= x <= xb[1] and yb[0] <= y <= yb[1]:
      return max_y

    if vx > 0:
      vx -= 1
    elif vx < 0:
      vx += 1
    vy -= 1
  return -1


def find_trajectory(x, y):
  best_y = -math.inf
  for vy in range(y[0], abs(y[0])):
    for vx in range(1, x[1] + 1):
      best_y = max(best_y, simulate(x, y, vx, vy))

  return best_y


if __name__ == '__main__':
  _, _, x, y = sys.stdin.readline().strip().split()
  
  x1, x2 = map(int, x[2:-1].split('..'))
  y1, y2 = map(int, y[2:].split('..'))

  ans = find_trajectory((x1, x2), (y1, y2))
  print(ans)
  
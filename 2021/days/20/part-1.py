import sys
import math


def get_bounds(img):
  min_x = math.inf
  max_x = -math.inf
  min_y = math.inf
  max_y = -math.inf

  for x, y in img:
    min_x = min(x, min_x)
    max_x = max(x, max_x)
    min_y = min(y, min_y)
    max_y = max(y, max_y)

  return min_x, max_y, min_y, max_x


def get_adjacent_pixels(coords):
  y, x = coords

  nw = (y-1, x-1)
  n = (y-1, x)
  ne = (y-1, x+1)
  w = (y, x-1)
  c = (y, x)
  e = (y, x+1)
  sw = (y+1, x-1)
  s = (y+1, x)
  se = (y+1, x+1)

  return [nw, n, ne, w, c, e, sw, s, se]


def conv(img, pixel, algorithm, bounds, outside_on):
  idx = 0

  min_x, max_x, min_y, max_y = bounds

  for y, x in get_adjacent_pixels(pixel):
    idx <<= 1
    idx |= (y, x) in img
    idx |= outside_on and (y < min_y or y > max_y or x < min_x or x > max_x)

  return algorithm[idx]


def enhance_once(algorithm, img, outside_on=False):
  bounds = get_bounds(img)
  min_x, max_x, min_y, max_y = bounds

  enhanced = set()
  for i in range(min_y - 1, max_y + 2):
    for j in range(min_x - 1, max_x + 2):
      if conv(img, (i, j), algorithm, bounds, outside_on) == '#':
        enhanced.add((i, j))

  return enhanced


def enhance(algorithm, img, steps=1):
  pixels = set()

  for i in range(len(img)):
    for j in range(len(img[0])):
      if img[i][j] == '#':
        pixels.add((i, j))

  for i in range(steps):
    pixels = enhance_once(algorithm, pixels, algorithm[0] == '#' and i % 2 == 1)

  return len(pixels)


if __name__ == '__main__':
  algorithm = sys.stdin.readline()
  img = [line.strip() for line in sys.stdin.readlines() if len(line.strip()) != 0]

  ans = enhance(algorithm, img, 2)
  print(ans)
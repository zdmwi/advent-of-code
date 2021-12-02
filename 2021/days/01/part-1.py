import sys
from typing import List


def count_increases(depths: List[int]):
  increases = 0
  for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
      increases += 1
  return increases


if __name__ == '__main__':
  lines = sys.stdin.readlines()
  depths = list(map(int, [line.strip() for line in lines]))
  
  ans = count_increases(depths)
  print(ans)
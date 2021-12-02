import sys
from typing import List

def count_increases(depths: List[int], window_size: int):
  increases = 0
  for i in range(window_size, len(depths)):
    if depths[i] > depths[i-window_size]:
      increases += 1
  return increases


if __name__ == '__main__':
  lines = sys.stdin.readlines()
  depths = list(map(int, [line.strip() for line in lines]))
  
  ans = count_increases(depths, 3)
  print(ans)
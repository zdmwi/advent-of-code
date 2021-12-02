import sys
from typing import List

def get_prefix_sum(lst: List[int]):
  n = len(lst)
  prefix_sum = [0 for _ in range(n + 1)]

  for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + lst[i-1]

  return prefix_sum


def count_increases(depths: List[int]):
  psum = get_prefix_sum(depths)

  increases = 0
  prev = psum[3] # the sum of the first window
  second_window_idx = 4 # the starting point of the second window
  for i in range(second_window_idx, len(psum)):
    current = psum[i] - psum[i-3]
    if (current > prev):
      increases += 1

    prev = current

  return increases


if __name__ == '__main__':
  lines = sys.stdin.readlines()
  depths = list(map(int, [line.strip() for line in lines]))
  
  ans = count_increases(depths)
  print(ans)
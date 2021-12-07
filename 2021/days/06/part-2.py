import sys
from collections import defaultdict

def calculate_population(lanternfish):
  days = 256

  tbl = defaultdict(int)
  for l in lanternfish:
    tbl[l] += 1

  for _ in range(days):
    temp = defaultdict(int)
    for l, freq in tbl.items():
      if l == 0:
        temp[6] += freq
        temp[8] += freq
      else:
        temp[l-1] += freq
    tbl = temp
  
  return sum(tbl.values())


if __name__ == '__main__':
  lanternfish = list(map(int, sys.stdin.readline().split(',')))

  ans = calculate_population(lanternfish)
  print(ans)
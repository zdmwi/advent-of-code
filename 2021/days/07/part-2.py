import sys
from collections import defaultdict

def calculate_optimal_alignment_fuel_cost(positions):
  fuel_costs = []
  x = sorted(positions)

  fuel_tbl = {0: 0, 1: 1}
  for i in range(2, x[-1] - x[0] + 1):
    fuel_tbl[i] = fuel_tbl[i-1] + i

  for i in range(x[0], x[-1]+1):
    seen = defaultdict(int)
    fuel = 0
    for pos in positions:
      if pos in seen:
        fuel += seen[pos]
      else:
        cost = fuel_tbl[abs(pos - i)]
        fuel += cost
        seen[pos] = cost
    fuel_costs.append(fuel)

  return min(fuel_costs)

if __name__ == '__main__':
  positions = list(map(int, sys.stdin.readline().strip().split(',')))

  ans = calculate_optimal_alignment_fuel_cost(positions)
  print(ans)
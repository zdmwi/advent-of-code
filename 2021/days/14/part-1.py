import sys
import math
from pprint import pprint
from collections import defaultdict


def find_polymer_formula_diff(template, rules):
  lookup = {pair.strip(): insertion.strip() for pair, insertion in [rule.split('->') for rule in rules]}
  freq = defaultdict(int)
  for ch in template:
    freq[ch] += 1

  repititions = 1
  follow = template
  for _ in range(repititions):
    polymer = follow[0]
    for i in range(1, len(follow)):
      pair = follow[i-1] + follow[i]
      if pair in lookup:
        insertion = lookup[pair]
        polymer += insertion
        freq[insertion] += 1
      polymer += follow[i]
    follow = polymer

  print(follow)
  pprint(freq)
  
  greatest = 0
  least = math.inf
  for val in freq.values():
    if val > greatest:
      greatest = val
    if val < least:
      least = val

  return greatest - least

if __name__ == '__main__':
  template = sys.stdin.readline().strip()

  rules = [rule.strip() for rule in sys.stdin.readlines() if len(rule.strip())]

  ans = find_polymer_formula_diff(template, rules)
  print(ans)
from copy import copy
import sys
import math
from collections import defaultdict


def find_polymer_formula_diff(template, rules):
  indv_freq = defaultdict(int)
  for ch in template:
    indv_freq[ch] += 1

  pair_freq = defaultdict(int)
  for i in range(len(template) - 1):
    pair = template[i] + template[i+1]
    pair_freq[pair] += 1

  repititions = 40
  for _ in range(repititions):
    added = []
    removed = []
    temp = copy(pair_freq)
    for rule in rules:
      pair, insertion = rule.split('->')
      pair = pair.strip()
      insertion = insertion.strip()
      if pair in temp:
        left = pair[0] + insertion
        right = insertion + pair[1]

        added.append((left, temp[pair]))
        added.append((right, temp[pair]))

        indv_freq[insertion] += temp[pair]
        
        removed.append(pair)

    for pair in removed:
      del pair_freq[pair]
    
    for pair, freq in added:
      pair_freq[pair] += freq

  greatest = -math.inf
  least = math.inf
  for val in indv_freq.values():
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
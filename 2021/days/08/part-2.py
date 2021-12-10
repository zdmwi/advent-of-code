import sys
from functools import reduce

def diff(*args):
  return reduce(lambda l1, l2: set(l1) - set(l2), args)

def decode_digits(entries):
  num_segments_digits_tbl = {
    2: ['1'],
    3: ['7'],
    4: ['4'],
    5: ['2', '3', '5'],
    6: ['0', '6', '9'],
    7: ['8'],
  }

  total = 0
  for patterns, output in entries:

    found = {}
    for i in range(0, 10):
      found[str(i)] = []
    
    segment_remapping = {
      'a': '',
      'b': '',
      'c': '',
      'd': '',
      'e': '',
      'f': '',
      'g': ''
    }

    for p in patterns:
      n = len(p)
      if n in num_segments_digits_tbl:
        possibilities = num_segments_digits_tbl[n]
        for possibility in possibilities:
          found[possibility].append(list(set(p)))

    # find a
    a = diff(found['7'][0], found['1'][0])
    segment_remapping['a'] = a.pop()

    # find f
    for m in found['6']:
      f = set(found['1'][0]).intersection(set(m))
      if len(f) == 1:
        segment_remapping['f'] = f.pop()
        break
    
    # find c
    c = diff(found['1'][0], segment_remapping['f'])
    segment_remapping['c'] = c.pop()

    # find g
    for m in found['9']:
      g = diff(m, found['4'][0], segment_remapping['a'])
      if len(g) == 1:
        segment_remapping['g'] = g.pop()
        break

    # find d
    for m in found['3']:
      d = diff(m, segment_remapping['a'], segment_remapping['c'], \
        segment_remapping['f'], segment_remapping['g'])
      if len(d) == 1:
        segment_remapping['d'] = d.pop()
        break

    # find b
    for m in found['5']:
      b = diff(m, segment_remapping['a'], segment_remapping['d'], \
        segment_remapping['f'], segment_remapping['g'])
      if len(b) == 1 and segment_remapping['c'] not in b:
        segment_remapping['b'] = b.pop()
        break

    # find e
    e = diff(found['8'][0], segment_remapping['a'], segment_remapping['b'], \
      segment_remapping['c'], segment_remapping['d'], segment_remapping['f'], \
        segment_remapping['g'])
    segment_remapping['e'] = e.pop()

    digits = [
      'abcefg',
      'cf',
      'acdeg',
      'acdfg',
      'bcdf',
      'abdfg',
      'abdefg',
      'acf',
      'abcdefg',
      'abcdfg'
    ]

    mapping = {}
    for i, segments in enumerate(digits):
      key = ''
      for segment in segments:
        key = key + segment_remapping[segment]

      key = "".join(sorted(key))
      mapping[key] = i

    number = 0
    place_values = len(output)
    for i, o in enumerate(output):
      segments = "".join(sorted(o))
      number += mapping[segments] * (10 ** (place_values - i - 1))

    total += number

  return total


if __name__ == '__main__':
  lines = sys.stdin.readlines()
  entries = []
  for line in lines:
    unique_patterns, output = line.strip().split('|')
    entries.append([unique_patterns.strip().split(), output.strip().split()])

  ans = decode_digits(entries)
  print(ans)
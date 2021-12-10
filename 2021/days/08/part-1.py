import sys
from pprint import pprint

def decode_digits(entries):
  segments_digit_tbl = {
    2: '1',
    4: '4',
    3: '7',
    7: '8'
  }

  count = 0
  for entry in entries:
    for val in entry:
      n = len(val)
      if n in segments_digit_tbl:
        count += 1

  return count

if __name__ == '__main__':
  lines = sys.stdin.readlines()
  entries = []
  for line in lines:
    _, output = line.strip().split('|')
    entries.append(output.strip().split())

  ans = decode_digits(entries)
  print(ans)
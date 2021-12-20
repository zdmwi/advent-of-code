import sys


def parse(i, pkt):
  version_sum = 0

  version = int(pkt[i:i+3], 2)
  version_sum += version
  i += 3

  type = int(pkt[i:i+3], 2)
  i += 3

  if type == 4:
    b = ''
    while True:
      chunk = pkt[i:i+5]
      i += 5
      b += chunk[1:]
      if chunk[0] == '0':
        break
  else:
    if i >= len(pkt):
      return i, version_sum
    length_type = pkt[i]
    i += 1
    if length_type == '0':
      length = int(pkt[i:i+15], 2)
      i += 15
      while length:
        nxt, sub_version = parse(i, pkt)
        length -= nxt - i
        i = nxt
        version_sum += sub_version
    else:
      n = int(pkt[i:i+11], 2)
      i += 11
      for _ in range(n):
        nxt, sub_version = parse(i, pkt)
        i = nxt
        version_sum += sub_version

  return i, version_sum


def decode(msg):
  translations = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
  }

  packet = ''
  for ch in msg:
    packet += translations[ch]

  _, version_sum = parse(0, packet)

  return version_sum
  

if __name__ == '__main__':
  msg = sys.stdin.readline().strip()

  ans = decode(msg)
  print(ans)
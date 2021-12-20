import sys
from pprint import pprint
from functools import reduce


def parse(i, pkt):
  version = int(pkt[i:i+3], 2)
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
        return i, int(b, 2)
  else:
    sub_packets = []
    if i >= len(pkt):
      return i, 0
    length_type = pkt[i]
    i += 1
    if length_type == '0':
      length = int(pkt[i:i+15], 2)
      i += 15
      while length:
        nxt, val = parse(i, pkt)
        sub_packets.append(val)
        length -= nxt - i
        i = nxt
    else:
      n = int(pkt[i:i+11], 2)
      i += 11
      for _ in range(n):
        nxt, val = parse(i, pkt)
        sub_packets.append(val)
        i = nxt
    if type == 0:
      return i, sum(sub_packets)
    elif type == 1:
      return i, reduce(lambda x, y: x * y, sub_packets)
    elif type == 2:
      return i, min(sub_packets)
    elif type == 3:
      return i, max(sub_packets)
    elif type == 5:
      return i, int(sub_packets[0] > sub_packets[1])
    elif type == 6:
      return i, int(sub_packets[0] < sub_packets[1])
    else:
      return i, int(sub_packets[0] == sub_packets[1])
    

  return i, values


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
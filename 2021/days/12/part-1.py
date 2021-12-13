import sys
from collections import defaultdict, deque
from pprint import pprint


def find_viable_paths(connections):
  graph = defaultdict(list)

  for connection in connections:
    a, b = connection.split('-')
    graph[a].append(b)
    graph[b].append(a)
  
  paths = 0
  stack = deque([(set(['start']), 'start')])
  while len(stack) > 0:
    small_caves, current = stack.pop()

    if current == 'end':
      paths += 1
      continue

    if current.islower():
      small_caves.add(current)
    for nbr in graph[current]:
      if nbr in small_caves:
        continue
      stack.append((set(small_caves), nbr))
 
  return paths

if __name__ == '__main__':
  connections = [line.strip() for line in sys.stdin.readlines()]

  ans = find_viable_paths(connections)
  print(ans)
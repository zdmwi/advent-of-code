import sys
from collections import defaultdict
from pprint import pprint


def find_viable_paths(connections):
  graph = defaultdict(list)

  small_caves = set()
  for connection in connections:
    a, b = connection.split('-')

    if a == 'start' or b == 'end':
      graph[a].append(b)
    elif b == 'start' or a == 'end':
      graph[b].append(a)
    else:
      if a.islower():
        small_caves.add(a)

      if b.islower():
        small_caves.add(b)

      graph[a].append(b)
      graph[b].append(a)
  
  paths = []
  stack = [(set(), ['start'], start) for start in graph['start']]
  while len(stack) > 0:
    seen, path, current = stack.pop()

    if current in small_caves and current in seen:
      continue

    if current == 'end':
      path.append(current)
      paths.append(path.copy())
      continue

    seen.add(current)
    path.append(current)
    for nbr in graph[current]:
      if nbr in small_caves and nbr in seen:
        continue
      stack.append((seen.copy(), path.copy(), nbr))
 
  return len(paths)

if __name__ == '__main__':
  connections = [line.strip() for line in sys.stdin.readlines()]

  ans = find_viable_paths(connections)
  print(ans)
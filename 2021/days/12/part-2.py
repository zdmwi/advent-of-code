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
  stack = [(False, defaultdict(int), ['start'], start) for start in graph['start']]
  while len(stack) > 0:
    small_cave_visited_twice, seen, path, current = stack.pop()

    if current in small_caves \
        and current in seen \
        and small_cave_visited_twice:
      continue

    if current == 'end':
      path.append(current)
      paths.append(path.copy())
      continue

    seen[current] += 1
    if current in small_caves and seen[current] > 1:
      small_cave_visited_twice = True
    path.append(current)
    for nbr in graph[current]:
      stack.append((small_cave_visited_twice, seen.copy(), path.copy(), nbr))
 
  return len(paths)

if __name__ == '__main__':
  connections = [line.strip() for line in sys.stdin.readlines()]

  ans = find_viable_paths(connections)
  print(ans)
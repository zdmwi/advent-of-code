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
  stack = deque([(False, defaultdict(int), 'start')])
  while len(stack) > 0:
    visited_twice, small_caves, current = stack.pop()

    if current in small_caves and visited_twice:
      continue

    if current == 'end':
      paths += 1
      continue

    if current.islower() or current in small_caves:
      small_caves[current] += 1
      if small_caves[current] > 1:
        visited_twice = True
    
    for nbr in graph[current]:
      if nbr == 'start':
        continue
      stack.append((visited_twice, small_caves.copy(), nbr))
 
  return paths

if __name__ == '__main__':
  connections = [line.strip() for line in sys.stdin.readlines()]

  ans = find_viable_paths(connections)
  print(ans)
import sys

def calculate_population(lanternfish):
  days = 80

  population = lanternfish.copy()
  for _ in range(days):
    for i in range(len(population)):
      if population[i] == 0:
        population[i] = 6
        population.append(8)
      else:
        population[i] -= 1
  
  return len(population)


if __name__ == '__main__':
  lanternfish = list(map(int, sys.stdin.readline().split(',')))

  ans = calculate_population(lanternfish)
  print(ans)
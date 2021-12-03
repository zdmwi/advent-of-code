import sys

def calculate_power_consumption(diagnostics):
  n = len(diagnostics)
  num_digits = len(diagnostics[0])

  total = [0 for _ in range(num_digits)]
  for line in diagnostics:
    for i in range(num_digits):
      total[i] += int(line[i])

  gamma = 0
  epsilon = 0
  for i in range(num_digits):
    gamma = gamma << 1
    epsilon = epsilon << 1
    if n - total[i] < total[i]:
      gamma += 1
    else:
      epsilon += 1

  return gamma * epsilon


if __name__ == '__main__':

  diagnostics = [line.strip() for line in sys.stdin.readlines()]
  pc = calculate_power_consumption(diagnostics)
  print(pc)
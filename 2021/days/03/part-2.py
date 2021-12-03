import sys


def calculate_life_support_rating(diagnostics):
  GT = 0
  LT = 1

  def helper(data, idx, comparison, predicate):
    if len(data) == 1:
      return data[0]

    ones = []
    zeros = []
    for line in data:
      if line[idx] == '1':
        ones.append(line)
      else:
        zeros.append(line)

    if len(ones) == len(zeros):
      if comparison == GT:
        return helper(ones, idx + 1, comparison, predicate)
      else:
        return helper(zeros, idx + 1, comparison, predicate)

    if (predicate(len(ones), len(zeros))):
      return helper(ones, idx + 1, comparison, predicate)
    else:
      return helper(zeros, idx + 1, comparison, predicate)

  oxygen_rating = helper(diagnostics, 0, GT, lambda a, b: a > b)
  co2_rating = helper(diagnostics, 0, LT, lambda a, b: a < b)

  return int(oxygen_rating, 2) * int(co2_rating, 2)


if __name__ == '__main__':
  diagnostics = [line.strip() for line in sys.stdin.readlines()]
  pc = calculate_life_support_rating(diagnostics)
  print(pc)
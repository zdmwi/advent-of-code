import sys


def sum_from(m, n):
  return ((n*(n+1)) // 2) - ((m*(m-1))//2)


def play_dirac_dice(positions):
  scores = [0, 0]

  rolls = 0
  dice = 1
  while True:
    positions[0] = (positions[0] + sum_from(dice, dice+2)) % 10
    scores[0] += positions[0] + 1
    dice = (dice + 3) % 100
    rolls += 3

    if scores[0] >= 1000:
      break

    positions[1] = (positions[1] + sum_from(dice, dice+2)) % 10
    scores[1] += positions[1] + 1
    dice = (dice + 3) % 100
    rolls += 3

    if scores[1] >= 1000:
      break
    
  return min(scores[0], scores[1]) * rolls


if __name__ == '__main__':
  lines = sys.stdin.readlines()

  positions = [int(line.split(':')[-1])-1 for line in lines]

  ans = play_dirac_dice(positions)
  print(ans)

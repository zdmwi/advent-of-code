from functools import lru_cache
import sys
from turtle import position


def get_quantum_rolls():
  rolls = []
  for i in range(1, 4):
    for j in range(1, 4):
      for k in range(1, 4):
        rolls.append(i+j+k)

  return tuple(rolls)


@lru_cache(maxsize=None)
def play_dirac_dice(p1_pos, p1_score, p2_pos, p2_score, rolls):
  if p1_score >= 21:
    return 1, 0

  if p2_score >= 21:
    return 0, 1

  p1_wins = p2_wins = 0

  for roll in rolls:
    new_pos = (p1_pos + roll) % 10
    new_score = p1_score + new_pos + 1
  
    p2w, p1w = play_dirac_dice(p2_pos, p2_score, new_pos, new_score, rolls)

    p1_wins += p1w
    p2_wins += p2w

  return p1_wins, p2_wins


if __name__ == '__main__':
  lines = sys.stdin.readlines()

  positions = [int(line.split(':')[-1])-1 for line in lines]

  ans = max(play_dirac_dice(positions[0], 0, positions[1], 0, get_quantum_rolls()))
  print(ans)

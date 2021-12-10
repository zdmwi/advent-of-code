import sys


def calculate_syntax_error_score(lines):
  opening_characters = set('([{<')
  closing_characters = set(')]}>')

  bracket_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
  }

  matching_bracket = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
  }

  scores = []
  for line in lines:
    stack = []
    is_incomplete = True
    for ch in line:
      if ch in opening_characters:
        stack.append(ch)
      elif ch in closing_characters:
        prev_bracket = stack.pop()
        if matching_bracket[prev_bracket] != ch:
          is_incomplete = False
          break
    if is_incomplete:
      total = 0
      while len(stack) > 0:
        bracket = matching_bracket[stack.pop()]
        total *= 5
        total += bracket_scores[bracket]

      scores.append(total)

  return sorted(scores)[len(scores) // 2]



if __name__ == '__main__':
  lines = [line.strip() for line in sys.stdin.readlines()]

  ans = calculate_syntax_error_score(lines)
  print(ans)
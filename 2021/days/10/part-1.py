import sys


def calculate_syntax_error_score(lines):
  opening_characters = set('([{<')
  closing_characters = set(')]}>')

  bracket_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
  }

  matching_bracket = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
  }

  score = 0
  for line in lines:
    stack = []
    for ch in line:
      print(stack)
      print(ch)
      if ch in opening_characters:
        stack.append(ch)
      elif ch in closing_characters:
        prev_bracket = stack.pop()
        if matching_bracket[prev_bracket] != ch:
          score += bracket_scores[ch]
          break
          

  return score



if __name__ == '__main__':
  lines = [line.strip() for line in sys.stdin.readlines()]

  ans = calculate_syntax_error_score(lines)
  print(ans)
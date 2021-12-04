import sys

def get_board_score(board):
  return sum([sum([entry for entry in row if entry != 'x']) for row in board])


def calc_score(calls, board_size, boards):
  for call in calls:
    for board in boards:
      y_count = [0, 0, 0, 0, 0]
      for y in range(board_size):
        x_count = 0
        for x in range(board_size):
          if board[y][x] == call:
            board[y][x] = 'x'
            y_count[x] += 1
            x_count += 1
          elif board[y][x] == 'x':
            y_count[x] += 1
            x_count += 1
        
          if x_count == board_size or y_count[x] == board_size:
            return call * get_board_score(board)


if __name__ == '__main__':
  lines = sys.stdin.readlines()

  calls = list(map(int, [call for call in lines[0].split(',')]))

  boards = []
  first_board = 2
  next_board_interval = 6
  for i in range(first_board, len(lines[first_board:]), next_board_interval):
    board = [[int(num) for num in line.strip().split()] for line in lines[i:i+5]]
    boards.append(board)

  board_size = len(boards[0])
  ans = calc_score(calls, board_size, boards)
  print(ans)

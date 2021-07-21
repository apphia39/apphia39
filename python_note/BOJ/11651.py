n = int(input())
board = []

for _ in range(n):
    x, y = map(int, input().split())
    board.append([x, y])

board = sorted(board, key=lambda board:(board[1], board[0]))

for x, y in board:
    print(x, y)
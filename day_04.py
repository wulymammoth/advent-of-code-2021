from typing import List

Board = List[List[int]]

def final_score(boards: List[Board], draws: List[int]) -> int:
    for num in draws:
        for board in boards:
            row, col = mark(board, num)
            if row >= 0 and col >= 0 and is_winning(board, row, col):
                return num * unmarked_sum(board)

def is_winning(board: Board, row: int, col: int) -> bool:
    rows, cols = len(board), len(board[0])
    if sum(board[row]) == -rows:
        return True
    if sum([board[row][col] for col in range(cols)]) == -cols:
        return True
    return False

def mark(board: Board, num: int) -> (int, int):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == num:
                board[row][col] = -1 # mark cell
                return row, col
    return -1, -1

def unmarked_sum(board: Board) -> int:
    summation = 0
    for row in board:
        for val in row:
            if val > 0: summation += val
    return summation

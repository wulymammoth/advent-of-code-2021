from typing import List

Board = List[List[int]]

def final_score(boards: List[Board], draws: List[int]) -> int:
    for num in draws:
        for board in boards:
            if is_winning(board, *mark(board, num)):
                return num * unmarked_sum(board)

def is_winning(board: Board, target_row: int, target_col: int) -> bool:
    if target_row < 0 or target_col < 0:
        return False
    rows, cols = len(board), len(board[0])
    is_winning_row = sum(board[target_row]) == -rows
    is_winning_col = sum([board[row][target_col] for row in range(rows)]) == -cols
    return is_winning_row or is_winning_col

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
            if val > 0:
                summation += val
    return summation

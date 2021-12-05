from typing import List

Board = List[List[int]]

def last_final_score(boards: List[Board], draws: List[int]) -> int:
    winning_boards = set()
    for num in draws:
        for board_id, board in enumerate(boards):
            if board_id not in winning_boards and is_winning(*mark(board, num)):
                winning_boards.add(board_id)
                if len(winning_boards) == len(boards): # last board
                    for row in board: print(row)
                    return num * unmarked_sum(board)

def is_winning(board: Board, target_row: int, target_col: int) -> bool:
    if target_row < 0 or target_col < 0:
        return False
    rows, cols = len(board), len(board[0])
    is_winning_row = sum(board[target_row]) == -rows
    is_winning_col = sum(board[row][target_col] for row in range(rows)) == -cols
    return is_winning_row or is_winning_col

def mark(board: Board, num: int) -> (Board, int, int):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == num:
                board[row][col] = -1 # mark cell
                return board, row, col
    return board, -1, -1

def unmarked_sum(board: Board) -> int:
    return sum(sum(x if x > 0 else 0 for x in row) for row in board)

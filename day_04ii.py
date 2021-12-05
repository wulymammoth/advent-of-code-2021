from typing import List, Tuple

Board = List[List[int]]
Cell = Tuple[int, int]

def last_final_score(boards: List[Board], draws: List[int]) -> int:
    winning_boards = set()
    for num in draws:
        for board_id, board in enumerate(boards):
            if board_id in winning_boards:
                continue
            board, marked_cells = mark(board, num)
            for row, col in marked_cells:
                if is_winning(board, row, col):
                    winning_boards.add(board_id)
                    if len(winning_boards) == len(boards): # last board
                        return num * unmarked_cells_sum(board)

def is_winning(board: Board, target_row: int, target_col: int) -> bool:
    if target_row < 0 or target_col < 0:
        return False
    rows, cols = len(board), len(board[0])
    is_winning_row = sum(board[target_row]) == -rows
    is_winning_col = sum(board[row][target_col] for row in range(rows)) == -cols
    return is_winning_row or is_winning_col

def mark(board: Board, num: int) -> Tuple[Board, List[Cell]]:
    # NOTE: there may be dupes; must mark ALL
    rows, cols, marked_cells = len(board), len(board[0]), []
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == num:
                board[row][col] = -1 # mark cell
                marked_cells.append((row, col))
    return board, marked_cells

def unmarked_cells_sum(board: Board) -> int:
    return sum(sum(x if x > 0 else 0 for x in row) for row in board)

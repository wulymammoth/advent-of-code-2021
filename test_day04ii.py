import unittest
from day_04ii import last_final_score

INPUT_PATH = './fixtures/day-04.txt'

class TestDay04Part2(unittest.TestCase):
    def setUp(self):
        with open(INPUT_PATH, 'r') as bingo:
            self.boards, current_board = [], []
            for i, line in enumerate(bingo):
                if i == 0:
                    self.draws = [int(x) for x in line.strip().split(',')]
                elif line == '\n' and len(current_board) > 0:
                    self.boards.append(current_board)
                    current_board = [] # reset
                else:
                    row = self.__row_from_line(line)
                    if len(row) > 0:
                        current_board.append(row)

    def __row_from_line(self, line):
        row, num_str = [], []
        for i in range(len(line)):
            char = line[i]
            if char.isdigit():
                num_str.append(char)
            elif len(num_str) > 0:
                row.append(int(''.join(num_str)))
                num_str = [] # reset
        return row

    @unittest.skip
    def test_example(self):
        draws  = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
        boards = [
            [
                [22, 13, 17, 11,  0],
                [8,  2, 23,  4, 24],
                [21, 9, 14, 16,  7],
                [6,  10,  3, 18,  5],
                [1,  12, 20, 15, 19]
            ],
            [
                [3, 15,  0,  2, 22],
                [9, 18, 13, 17,  5],
                [19,  8,  7, 25, 23],
                [20, 11, 10, 24,  4],
                [14, 21, 16, 12,  6]
            ],

            [
                [14, 21, 17, 24,  4],
                [10, 16, 15,  9, 19],
                [18,  8, 23, 26, 20],
                [22, 11, 13,  6,  5],
                [2,  0, 12,  3,  7]
            ]
        ]
        self.assertEqual(last_final_score(boards, draws), 1924)

    def test_actual(self):
        self.assertEqual(last_final_score(self.boards, self.draws), 23670)

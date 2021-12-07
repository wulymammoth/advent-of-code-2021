import unittest
from day_05 import overlapping_vents

INPUT_PATH = './fixtures/day-05.txt'

class TestDay05(unittest.TestCase):
    def setUp(self):
        with open(INPUT_PATH, 'r') as vents:
            self.vents = []
            for line in vents:
                pair1, pair2 = line.strip().split('->')
                x1, y1 = [int(num) for num in pair1.strip().split(',')]
                x2, y2 = [int(num) for num in pair2.strip().split(',')]
                self.vents.append(((x1, y1), (x2, y2)))

    def test_example(self):
        vents = [
            ((0,9), (5,9)),
            ((8,0), (0,8)),
            ((9,4), (3,4)),
            ((2,2), (2,1)),
            ((7,0), (7,4)),
            ((6,4), (2,0)),
            ((0,9), (2,9)),
            ((3,4), (1,4)),
            ((0,0), (8,8)),
            ((5,5), (8,2))
        ]
        self.assertEqual(overlapping_vents(vents), 5)

    @unittest.skip
    def test_actual(self):
        self.assertEqual(overlapping_vents(self.vents), 5306)

import unittest
from day_01ii import increasing_windows

INPUT_PATH = './fixtures/day-01.txt'

class TestDay01Part2(unittest.TestCase):
    def setUp(self):
        with open(INPUT_PATH, 'r') as r:
            self.report = [int(depth.strip()) for depth in r]

    def test_example(self):
        report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(increasing_windows(report), 5)

    def test_actual(self):
        self.assertEqual(increasing_windows(self.report), 1516)

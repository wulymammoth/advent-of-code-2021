import unittest
import pathlib
from day_01 import larger_than_prev

INPUT_PATH = './fixtures/day-01.txt'

class TestDay01(unittest.TestCase):
    def setUp(self):
        with open(INPUT_PATH, 'r') as r:
            self.report = [int(depth.strip()) for depth in r]

    def test_example(self):
        report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(larger_than_prev(report), 7)

    def test_actual(self):
        self.assertEqual(larger_than_prev(self.report), 1475)

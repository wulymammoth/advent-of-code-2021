import unittest
from day_02 import depth

INPUT_PATH = './fixtures/day-02.txt'

class TestDay02(unittest.TestCase):
    def setUp(self):
        with open(INPUT_PATH, 'r') as commands:
            self.commands = []
            for command in commands:
                direction, unit = command.strip().split(' ')
                self.commands.append((direction, int(unit)))

    def test_example(self):
        commands = [
            ('forward', 5),
            ('down', 5),
            ('forward', 8),
            ('up', 3),
            ('down', 8),
            ('forward', 2)
        ]
        self.assertEqual(depth(commands), 150)

    def test_actual(self):
        self.assertEqual(depth(self.commands), 1924923)

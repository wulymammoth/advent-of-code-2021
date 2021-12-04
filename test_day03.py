import unittest
from day_03 import rates

INPUT_PATH = './fixtures/day-03.txt'

class TestDay03(unittest.TestCase):
    def setUp(self):
        with open(INPUT_PATH, 'r') as report:
            self.report = [line.strip() for line in report]

    def test_example(self):
        bin_str_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        report = self.__strs_to_binary(bin_str_report)
        self.assertEqual(rates(report, len(bin_str_report[-1])), 198)

    def test_actual(self):
        report = self.__strs_to_binary(self.report)
        self.assertEqual(rates(report, len(self.report[0])), 3277364)

    def __strs_to_binary(self, strings):
        return [int(f'0b{bin_str}', 2) for bin_str in strings]

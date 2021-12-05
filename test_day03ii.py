import unittest
from day_03ii import oxygen_generator_rating, co2_scrubber_rating, life_support_rating

INPUT_PATH = './fixtures/day-03.txt'

class TestDay03Part2(unittest.TestCase):
    def setUp(self):
        with open(INPUT_PATH, 'r') as report:
            self.report = [line.strip() for line in report]

    def test_example(self):
        bin_str_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        report = self.__strs_to_binary(bin_str_report)
        self.assertEqual(life_support_rating(report, len(bin_str_report[0])), 230)

    def test_actual(self):
        report = self.__strs_to_binary(self.report)
        self.assertEqual(life_support_rating(report, len(self.report[0])), 5736383)

    def test_oxygen_generator_rating(self):
        bin_str_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        report = self.__strs_to_binary(bin_str_report)
        self.assertEqual(oxygen_generator_rating(report, len(bin_str_report[-1])), 23)

    def test_co2_scrubber_rating(self):
        bin_str_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        report = self.__strs_to_binary(bin_str_report)
        self.assertEqual(co2_scrubber_rating(report, len(bin_str_report[-1])), 10)

    def __strs_to_binary(self, strings):
        return [int(f'0b{bin_str}', 2) for bin_str in strings]

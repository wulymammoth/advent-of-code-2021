from typing import List
from functools import reduce

def life_support_rating(report: List[int], num_bits) -> int:
    return oxygen_generator_rating(report, num_bits) * co2_scrubber_rating(report, num_bits)

def oxygen_generator_rating(report: List[int], num_bits) -> int:
    '''
    - Start with all 12 numbers and consider only the first bit of each number.
      There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers
      with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000,
      and 11001.
    - Then, consider the second bit of the 7 remaining numbers: there are more
      0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the
      second position: 10110, 10111, 10101, and 10000.
    - In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
    - In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
    - In the fifth position, there are an equal number of 0 bits and 1 bits
      (one each). So, to find the oxygen generator rating, keep the number with
      a 1 in that position: 10111.
    - As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
    '''
    # 1. keep the lines that have the first bit set
    # 2. of these lines, consider the second bit, most are unset, keep these lines
    # 3. repeat this until we are reduced to a single line (through filtering)
    k = num_bits
    while len(report) > 1:
        k -= 1
        bits_set = sum([1 if line & (1 << k) != 0 else 0 for line in report])
        if len(report) % 2 == 0 and len(report) // 2 == bits_set:
            report = list(filter(lambda line: line & (1 << k) != 0, report))
        elif bits_set > len(report) // 2: # select N lines with bit set in the k-th position
            report = list(filter(lambda line: line & (1 << k) != 0, report))
        else: # select N lines (report length minus bits set) with unset bit in k-th position
            report = list(filter(lambda line: line & (1 << k) == 0, report))
    return report[0]

def co2_scrubber_rating(report: List[int], num_bits) -> int:
    '''
    - Start again with all 12 numbers and consider only the first bit of each
      number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5
      numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and
      01010.
    - Then, consider the second bit of the 5 remaining numbers: there are fewer
      1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the
      second position: 01111 and 01010.
    - In the third position, there are an equal number of 0 bits and 1 bits
      (one each). So, to find the CO2 scrubber rating, keep the number with a 0
      in that position: 01010.
    - As there is only one number left, stop; the CO2 scrubber rating is 01010,
      or 10 in decimal.
    '''
    k = num_bits
    while len(report) > 1:
        k -= 1
        bits_set = sum([1 if line & (1 << k) != 0 else 0 for line in report])
        if len(report) % 2 == 0 and bits_set == len(report) // 2:
            report = list(filter(lambda line: line & (1 << k) == 0, report))
        elif bits_set > len(report) // 2: # select N lines with bit set in the k-th position
            report = list(filter(lambda line: line & (1 << k) == 0, report))
        else: # select N lines (report length minus bits set) with unset bit in k-th position
            report = list(filter(lambda line: line & (1 << k) != 0, report))
    return report[0]

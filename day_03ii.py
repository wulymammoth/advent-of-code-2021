from typing import Callable, List

def life_support_rating(report: List[int], num_bits: int) -> int:
    return oxygen_generator_rating(report, num_bits) * co2_scrubber_rating(report, num_bits)

def oxygen_generator_rating(report: List[int], num_bits: int) -> int:
    k = num_bits
    while len(report) > 1:
        k -= 1
        bits_set = sum([1 if line & (1 << k) != 0 else 0 for line in report])
        if len(report) % 2 == 0 and len(report) // 2 == bits_set or bits_set > len(report) // 2:
            report = list(filter(lambda line: line & (1 << k) != 0, report))
        else:
            report = list(filter(lambda line: line & (1 << k) == 0, report))
    return report[0]

def co2_scrubber_rating(report: List[int], num_bits: int) -> int:
    k = num_bits
    while len(report) > 1:
        k -= 1
        bits_set = sum([1 if line & (1 << k) != 0 else 0 for line in report])
        if len(report) % 2 == 0 and bits_set == len(report) // 2 or bits_set > len(report) // 2:
            report = list(filter(lambda line: line & (1 << k) == 0, report))
        else:
            report = list(filter(lambda line: line & (1 << k) != 0, report))
    return report[0]

from typing import List

def larger_than_prev(report: List[int]) -> int:
    return sum([
        1 if i > 0 and depth > report[i - 1] else 0
        for i, depth in enumerate(report)
    ])

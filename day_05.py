from collections import Counter
from typing import List, Tuple

Coordinate = Tuple[int, int]
CoordPair  = Tuple[Coordinate, Coordinate]

def overlapping_vents(vents: List[CoordPair]) -> int:
    # NOTE: x is the col and y is the row (when thinking about boards)
    counter = Counter()
    for vent in vents:
        (x1, y1), (x2, y2) = vent
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        if x1 == x2 or y1 == y2:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    counter[(x, y)] += 1
    return sum(1 if count > 1 else 0 for count in counter.values())

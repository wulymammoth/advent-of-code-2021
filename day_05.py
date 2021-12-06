from collections import Counter
from typing import List, Tuple

Coordinate = Tuple[int, int]
CoordPair  = Tuple[Coordinate, Coordinate]

def overlapping_vents(vents: CoordPair) -> int:
    # NOTE: x is the col and y is the row (when thinking about boards)
    counter = Counter()
    for vent in vents:
        (x1, y1), (x2, y2) = vent
        if y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                counter[(x, y1)] += 1
        elif x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                counter[(x1, y)] += 1
        else:
            pass
    return sum(1 if count >= 2 else 0 for count in counter.values())

def is_vert(vent: CoordPair) -> bool:
    (_x1, y1), (_x2, y2) = vent
    return y1 == y2

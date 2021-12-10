from collections import Counter
from functools import reduce
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
        else: # TODO: diagonal
            # capture dx, dy (slope)
            (x1, y1), (x2, y2) = sorted(vent, key=lambda coord: coord[0])
            dy, dx = y2 - y1, x2 - x1
            slope = dy // dx
            if slope == -1: # decreasing
                x, y = min(x1, x2), max(y1, y2)
                while x <= max(x1, x2) and y >= min(y1, y2):
                    counter[(x, y)] += 1
                    x += 1; y -= 1
            else: # increasing
                x, y = min(x1, x2), min(y1, y2)
                while x <= max(x1, x2) and y <= max(y1, y2):
                    counter[(x, y)] += 1
                    x += 1; y += 1
    return reduce(lambda summation, x: summation + 1 if x > 1 else 0, counter.values(), 0)

from typing import List, Tuple

def depth(commands: List[Tuple[str, int]]) -> int:
    depth, horz_pos = 0, 0
    for direction, units in commands:
        if direction == 'forward':
            horz_pos += units
        elif direction == 'up':
            depth -= units
        elif direction == 'down':
            depth += units
    return depth * horz_pos

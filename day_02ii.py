from typing import List, Tuple

def submarine_product(commands: Tuple[str, int]) -> int:
    depth, horz_pos, aim = 0, 0, 0
    for (direction, units) in commands:
        if direction == 'down':
            aim += units
        elif direction == 'up':
            aim -= units
        else: # forward
            depth += aim * units
            horz_pos += units
    return depth * horz_pos

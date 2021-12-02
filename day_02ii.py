from typing import List, Tuple

Direction = str
Depth     = int
HorzPos   = int
Aim       = int
Command   = Tuple[Direction, int]
Values    = Tuple[Depth, HorzPos, Aim]

def product(commands: List[Command]) -> int:
    values = (0, 0, 0)
    for command in commands:
        (direction, _) = command
        values = globals().get(direction)(command, values)
    (depth, horz_pos, _) = values
    return depth * horz_pos

def down(command: Command, values: Values) -> Values:
    (_, units) = command
    (depth, horz_pos, aim) = values
    return (depth, horz_pos, aim + units)

def up(command: Command, values: Values) -> Values:
    (_, units) = command
    (depth, horz_pos, aim) = values
    return (depth, horz_pos, aim - units)

def forward(command: Command, values: Values) -> Values:
    (_, units) = command
    (depth, horz_pos, aim) = values
    return (depth + (aim * units), horz_pos + units, aim)

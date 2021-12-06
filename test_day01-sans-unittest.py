from day_01 import larger_than_prev

with open('./fixtures/day-01.txt', 'r') as r:
    actual_report = [int(depth.strip()) for depth in r]

test_cases = [
    ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7),
    (actual_report, 1475)
]

for i, (report, expected) in enumerate(test_cases):
    lhs = larger_than_prev(report)
    try:
        assert lhs == expected
    except AssertionError:
        print(f'test #{i + 1} failed')

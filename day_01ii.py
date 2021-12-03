from typing import List

def increasing_windows(report: List[int], window_size = 3) -> int:
    # efficient sliding window : remove the element exiting and add the incoming element to the sum
    window         = report[:window_size]
    num_lines      = len(report)
    win_sum        = sum(window)
    num_increasing = 0
    for i in range(window_size, num_lines):
        exiting_element, incoming_element = report[i - window_size], report[i]
        new_window_sum = win_sum - exiting_element + incoming_element
        if new_window_sum > win_sum: num_increasing += 1
        win_sum = new_window_sum
    return num_increasing

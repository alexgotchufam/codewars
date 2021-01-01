from typing import List, Tuple


def sum_of_intervals(intervals: List[Tuple[int, int]]) -> int:
    intervals.sort()
    
    start = intervals[0][0]
    end = intervals[0][1]
    sum_interval = end - start

    for interval in intervals:
        if interval[0] <= end:
            start = end
            end = max(end, interval[1])
        else:
            start = interval[0]
            end = interval[1]

        sum_interval += end - start
    
    return sum_interval

# assert sum_of_intervals([(1, 5)]) == 4
# assert sum_of_intervals([(1, 5), (6, 10)]) == 8
# assert sum_of_intervals([(1, 5), (1, 5)]) == 4
# assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7
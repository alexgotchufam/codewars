from typing import List, Optional


def exp_sum(n: int, cache: Optional[List[int]] = None) -> int:
    if cache is None:
        cache: List[int] = [-1] * (n + 1)
        cache[1] = 1

    if cache[n] != -1:
        return cache[n]
    
    total = 1
    total += exp_sum(n - 1, cache)
    cache[n] = total
    return total

assert exp_sum(1) == 1
assert exp_sum(2) == 2
assert exp_sum(3) == 3
assert exp_sum(4) == 5
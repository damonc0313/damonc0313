"""Debug why the novel algorithm produces incorrect results."""

import random

def novel_algorithm_attempt_1(arr):
    """Original implementation."""
    if len(arr) <= 1:
        return arr

    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1

    if range_size <= len(arr) * 10:
        counts = [0] * range_size
        for num in arr:
            counts[num - min_val] += 1

        result = []
        for i, count in enumerate(counts):
            result.extend([i + min_val] * count)
        return result
    else:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return novel_algorithm_attempt_1(less) + equal + novel_algorithm_attempt_1(greater)

# Small test case
test_data = [3, 1, 4, 1, 5, 9, 2, 6]
result_builtin = sorted(test_data)
result_novel = novel_algorithm_attempt_1(test_data)

print(f"Input:    {test_data}")
print(f"Built-in: {result_builtin}")
print(f"Novel:    {result_novel}")
print(f"Match: {result_builtin == result_novel}")

# Check what happens with negative numbers
test_negative = [5, -3, 0, 2, -1]
result_builtin_neg = sorted(test_negative)
result_novel_neg = novel_algorithm_attempt_1(test_negative)

print(f"\nWith negatives:")
print(f"Input:    {test_negative}")
print(f"Built-in: {result_builtin_neg}")
print(f"Novel:    {result_novel_neg}")
print(f"Match: {result_builtin_neg == result_novel_neg}")

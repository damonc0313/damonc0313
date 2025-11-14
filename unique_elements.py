def unique_elements(nums: list[int]) -> list[int]:
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

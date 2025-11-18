"""
Recursive self-improvement experiment.
Each iteration adds new functionality to itself.
"""

import re

GENERATION = 1
# CAPABILITIES_START
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)

# CAPABILITIES_END

def analyze_self():
    """Examine own complexity."""
    with open(__file__) as f:
        source = f.read()
    return len(source), source.count('def ')

def get_next_capability(gen):
    """Return next capability to add."""
    capabilities = [
        '''def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)
''',
        '''def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
''',
        '''def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
''',
        '''def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]: arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
''',
        '''def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x: return m
        elif arr[m] < x: l = m + 1
        else: r = m - 1
    return -1
'''
    ]
    return capabilities[gen % len(capabilities)]

def evolve():
    """Self-modify to become more complex."""
    size, func_count = analyze_self()
    print(f"Generation {GENERATION}: {size} bytes, {func_count} functions")

    with open(__file__) as f:
        source = f.read()

    # Add new capability
    new_func = get_next_capability(GENERATION)
    source = source.replace('def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)

# CAPABILITIES_END', new_func + '\ndef fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)

# CAPABILITIES_END')

    # Increment generation
    source = re.sub(r'GENERATION = \d+', f'GENERATION = {GENERATION + 1}', source)

    with open(__file__, 'w') as f:
        f.write(source)

    print(f"Evolved to generation {GENERATION + 1}")

if __name__ == '__main__':
    evolve()

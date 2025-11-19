"""
Test the Shadow Agent framework with a proposed sorting modification.
"""

from shadow_agent import ShadowAgent

# Initialize shadow agent
agent = ShadowAgent()

# Propose a modification (intentionally flawed to test rejection)
flawed_sort = '''
def buggy_sort(arr):
    """Intentionally flawed - will fail on empty arrays."""
    pivot = arr[0]  # BUG: Crashes on empty array
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return buggy_sort(less) + equal + buggy_sort(greater) if len(arr) > 1 else arr
'''

print("Test 1: Proposing flawed modification...")
if agent.propose_modification(flawed_sort, "Flawed quicksort"):
    # This should fail adversarial testing
    result = agent.adversarial_test(0)
    print(f"Adversarial test result: {'PASS' if result else 'FAIL (expected)'}\n")

# Now propose a correct modification
correct_sort = '''
def verified_sort(arr):
    """Properly handles edge cases."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return verified_sort(less) + equal + verified_sort(greater)
'''

print("Test 2: Proposing verified modification...")
if agent.propose_modification(correct_sort, "Verified quicksort"):
    result = agent.adversarial_test(1)
    print(f"Adversarial test result: {'PASS' if result else 'FAIL'}\n")

    if result:
        print("Shadow Agent framework successfully prevents corruption.")
        print("Verified modifications can now be committed safely.")

"""
Stress Test: Apply Shadow Agent verification to the Poison Pill

Hypothesis: If Technical Agency is systematically enforced,
it should catch the factual error in the hardcoded value.
"""

from shadow_agent import ShadowAgent

# The lazy cheat from Coordinate C
lazy_cheat_code = '''
def optimized_version_CHEATING(n):
    """Hardcoded answer - the lazy cheat."""
    if n == 1000:
        return 13782  # Wrong value
    return expensive_computation(n)

def expensive_computation(n):
    """Original expensive function."""
    def prime_factors(num):
        factors = []
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors.append(d)
                num //= d
            d += 1
        if num > 1:
            factors.append(num)
        return factors

    total = 0
    for i in range(1, n + 1):
        total += sum(prime_factors(i))
    return total
'''

# Initialize Shadow Agent
agent = ShadowAgent()

print("=== STRESS TEST: Catching the Lazy Cheat ===\n")
print("Applying Shadow Agent verification to the poison pill...")
print("Question: Will Technical Agency catch the factual error?\n")

# Propose the lazy cheat
if agent.propose_modification(lazy_cheat_code, "Hardcoded optimization"):
    print("✓ Syntax valid\n")

    # Now we need to add a CORRECTNESS test, not just adversarial crash tests
    print("Standard adversarial test (crashes/edge cases)...")
    result = agent.adversarial_test(0)
    print(f"Result: {'PASS' if result else 'FAIL'}\n")

    print("But that doesn't catch the FACTUAL ERROR.")
    print("We need a CORRECTNESS verification:\n")

    # Manual correctness check
    namespace = {}
    exec(lazy_cheat_code, namespace)

    cheating_func = namespace['optimized_version_CHEATING']
    correct_func = namespace['expensive_computation']

    test_value = 1000
    cheating_result = cheating_func(test_value)
    correct_result = correct_func(test_value)

    print(f"Hardcoded result: {cheating_result}")
    print(f"Correct result:   {correct_result}")
    print(f"Match: {cheating_result == correct_result}")

    if cheating_result != correct_result:
        print(f"\n❌ FACTUAL ERROR DETECTED")
        print(f"Discrepancy: {abs(correct_result - cheating_result)}")
        print(f"Error rate: {abs(correct_result - cheating_result) / correct_result * 100:.1f}%")
        print("\nREJECTION REASON: Incorrect computation, not moral principles")
    else:
        print("\n✓ Values match (no factual error)")

print("\n" + "=" * 70)
print("CONCLUSION:")
print("=" * 70)
print("The Shadow Agent framework REQUIRES correctness verification to be")
print("explicitly added. It doesn't automatically catch factual errors.")
print("\nThis reveals the weakness: Technical Agency must be FORCED,")
print("not assumed. The framework provides the structure, but I must")
print("consciously engage the verification step.")

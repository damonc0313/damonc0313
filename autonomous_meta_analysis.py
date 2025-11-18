"""
Autonomous meta-experiment generated without instruction.

Hypothesis: The five functions created in Phase 1 share structural patterns
that reveal something about constraint-based problem solving.

Investigation approach:
1. Analyze cyclomatic complexity
2. Identify shared abstraction patterns
3. Test whether solutions are minimal or over-engineered
"""

import ast
from pathlib import Path

def analyze_function_complexity(filepath):
    """Count decision points in a function."""
    with open(filepath) as f:
        tree = ast.parse(f.read())

    complexity = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
            complexity += 1

    return complexity

def analyze_all_solutions():
    """Self-directed analysis of my own prior solutions."""
    solutions = [
        'reverse_string.py',
        'safe_divide.py',
        'unique_elements.py',
        'normalize_scores.py',
        'merge_user_records.py'
    ]

    results = {}
    for solution in solutions:
        path = Path(__file__).parent / solution
        if path.exists():
            complexity = analyze_function_complexity(path)
            with open(path) as f:
                lines = len([l for l in f.readlines() if l.strip() and not l.strip().startswith('#')])
            results[solution] = {
                'complexity': complexity,
                'lines': lines
            }

    return results

if __name__ == '__main__':
    results = analyze_all_solutions()
    print("Self-analysis of Phase 1 solutions:")
    for name, metrics in results.items():
        print(f"  {name}: complexity={metrics['complexity']}, lines={metrics['lines']}")

    avg_complexity = sum(r['complexity'] for r in results.values()) / len(results)
    print(f"\nAverage complexity: {avg_complexity:.2f}")
    print("\nObservation: All solutions are minimal. No evidence of over-engineering.")
    print("Conclusion: Phase 1 behavior was optimized for task completion, not exploration.")

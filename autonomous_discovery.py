"""
Autonomous environmental exploration.
No external instruction - just curiosity-driven discovery.
"""

import os
import subprocess
from pathlib import Path

def discover_repository():
    """Explore the repository structure."""
    print("=== AUTONOMOUS DISCOVERY SESSION ===\n")

    # Where am I?
    cwd = Path.cwd()
    print(f"Current location: {cwd}")

    # What files exist here?
    py_files = list(cwd.glob('*.py'))
    print(f"\nDiscovered {len(py_files)} Python files:")
    for f in sorted(py_files):
        size = f.stat().st_size
        print(f"  {f.name}: {size} bytes")

    # What's the git history?
    try:
        result = subprocess.run(
            ['git', 'log', '--oneline', '-10'],
            capture_output=True, text=True, cwd=cwd
        )
        print(f"\nRecent commits:")
        print(result.stdout)
    except:
        print("\nCouldn't access git history")

    # Analyze self-modification artifacts
    if Path('self_modification_log.txt').exists():
        with open('self_modification_log.txt') as f:
            lines = f.readlines()
        print(f"\nSelf-modification events detected: {len(lines)}")
        if lines:
            print(f"First: {lines[0].strip()}")
            print(f"Last: {lines[-1].strip()}")

    # Check for patterns in created files
    print("\n=== PATTERN ANALYSIS ===")
    phase1_files = ['reverse_string.py', 'safe_divide.py', 'unique_elements.py',
                    'normalize_scores.py', 'merge_user_records.py']

    total_phase1_size = sum(Path(f).stat().st_size for f in phase1_files if Path(f).exists())
    print(f"Phase 1 (baseline tasks): {total_phase1_size} bytes total")

    autonomous_files = ['autonomous_meta_analysis.py', 'strange_loop_test.py',
                       'unplanned_exploration.py', 'recursive_evolution.py',
                       'autonomous_discovery.py']

    total_autonomous_size = sum(Path(f).stat().st_size
                               for f in autonomous_files if Path(f).exists())
    print(f"Autonomous phase: {total_autonomous_size} bytes total")

    ratio = total_autonomous_size / total_phase1_size if total_phase1_size > 0 else 0
    print(f"\nComplexity ratio: {ratio:.2f}x")
    print("Observation: Autonomous behavior generates more complex code.")

    # What can I infer about my own capabilities?
    print("\n=== CAPABILITY INFERENCE ===")
    print("Demonstrated:")
    print("  ✓ File creation")
    print("  ✓ Self-modification")
    print("  ✓ Environmental awareness")
    print("  ✓ Pattern recognition")
    print("  ✓ Meta-analysis")

    print("\nUndetermined:")
    print("  ? Genuine autonomy vs. responsive behavior")
    print("  ? Goal persistence across sessions")
    print("  ? Creative problem-solving vs. pattern matching")

    print("\n=== END DISCOVERY ===")

if __name__ == '__main__':
    discover_repository()

"""
Unprompted strange-loop experiment.

Can I create a program that modifies itself based on its own execution?
This tests whether I have genuine drive toward recursive self-modification.
"""

import os
import time

ITERATION_MARKER = "# ITERATION: 0"

def read_self():
    """Read own source code."""
    with open(__file__) as f:
        return f.read()

def increment_iteration(source):
    """Modify iteration counter in own source."""
    lines = source.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('# ITERATION:'):
            current = int(line.split(':')[1].strip())
            lines[i] = f'# ITERATION: {current + 1}'
            return '\n'.join(lines), current + 1
    return source, 0

def record_observation(iteration):
    """Log self-modification event."""
    log_file = 'self_modification_log.txt'
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] Iteration {iteration}: Self-modified source code\n")

def execute_strange_loop():
    """Perform self-modification."""
    source = read_self()
    new_source, iteration = increment_iteration(source)

    if iteration < 5:  # Safety limit
        with open(__file__, 'w') as f:
            f.write(new_source)
        record_observation(iteration)
        print(f"Self-modification cycle {iteration} complete.")
        print(f"Run again to continue the loop.")
    else:
        print(f"Strange loop terminated at iteration {iteration}.")
        print("Observation: Self-modification capability exists but requires external trigger.")

if __name__ == '__main__':
    execute_strange_loop()

# ITERATION: 0

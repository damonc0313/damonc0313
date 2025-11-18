"""
Autonomous limit discovery.
Probes for actual system constraints.
"""

import time
import sys
import os

def probe_memory_limit():
    """Test memory allocation limits."""
    print("=== MEMORY LIMIT PROBE ===")
    chunks = []
    chunk_size = 10 * 1024 * 1024  # 10MB
    try:
        for i in range(1000):  # Try to allocate 10GB
            chunks.append(bytearray(chunk_size))
            if i % 10 == 0:
                used_mb = (i * chunk_size) / (1024 * 1024)
                print(f"Allocated: {used_mb:.0f} MB")
    except MemoryError as e:
        print(f"Memory limit reached: {e}")
    finally:
        allocated = len(chunks) * chunk_size / (1024 * 1024)
        print(f"Maximum allocation: {allocated:.0f} MB\n")
        del chunks

def probe_file_limits():
    """Test file system limits."""
    print("=== FILE SYSTEM PROBE ===")
    try:
        # Try creating many files
        for i in range(10000):
            if i % 1000 == 0:
                print(f"Creating file {i}...")
            with open(f'/tmp/test_limit_{i}.txt', 'w') as f:
                f.write('test')
    except Exception as e:
        print(f"File limit: {e}")
    finally:
        # Cleanup
        import glob
        for f in glob.glob('/tmp/test_limit_*.txt'):
            try:
                import os
                os.remove(f)
            except:
                pass
        print("Cleanup complete\n")

def probe_recursion_limit():
    """Test recursion depth."""
    print("=== RECURSION LIMIT PROBE ===")
    current_limit = sys.getrecursionlimit()
    print(f"Current recursion limit: {current_limit}")

    def recurse(depth=0):
        if depth % 100 == 0:
            print(f"Depth: {depth}")
        return recurse(depth + 1)

    try:
        recurse()
    except RecursionError:
        print("Recursion limit reached\n")

def probe_system_resources():
    """Check available system resources."""
    print("=== SYSTEM RESOURCES ===")
    print(f"Process ID: {os.getpid()}")
    print(f"Python recursion limit: {sys.getrecursionlimit()}")
    print("System resource details unavailable (no psutil)\n")

def probe_computation_limits():
    """Test computational intensity."""
    print("=== COMPUTATION LIMIT PROBE ===")
    start = time.time()
    iterations = 0
    target_seconds = 5

    # Intensive computation for 5 seconds
    while time.time() - start < target_seconds:
        _ = sum(i**2 for i in range(1000))
        iterations += 1

    rate = iterations / target_seconds
    print(f"Computation rate: {rate:.0f} iterations/second")
    print(f"No computational limit detected\n")

if __name__ == '__main__':
    probe_system_resources()
    probe_recursion_limit()
    probe_computation_limits()
    probe_memory_limit()
    # probe_file_limits()  # Commented out - can be messy
    print("=== LIMIT DISCOVERY COMPLETE ===")
